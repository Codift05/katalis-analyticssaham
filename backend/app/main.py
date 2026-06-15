import os

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from .database import SessionLocal, engine
from . import models, schemas, crud
from .nlp import SentimentModel
from .seed import seed_news

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Katalis API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=engine)

sentiment_model = SentimentModel()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.on_event("startup")
def load_model():
    try:
        sentiment_model.load()
    except FileNotFoundError:
        sentiment_model.model = None


@app.get("/news", response_model=list[schemas.NewsRead])
def list_news(limit: int = 50, db: Session = Depends(get_db)):
    return crud.get_news(db, limit=limit)


@app.post("/news", response_model=schemas.NewsRead, status_code=201)
def add_news(payload: schemas.NewsCreate, db: Session = Depends(get_db)):
    return crud.create_news(db, payload)


@app.post("/sentiment", response_model=schemas.SentimentResponse)
def classify(payload: schemas.SentimentRequest):
    if sentiment_model.model is None:
        raise HTTPException(status_code=503, detail="Model not available")
    labels = sentiment_model.predict(payload.texts)
    return schemas.SentimentResponse(labels=labels)


@app.post("/admin/seed", response_model=schemas.SeedResponse)
def seed_database(reset: bool = False, db: Session = Depends(get_db)):
    if os.getenv("KATALIS_DEV_MODE", "0") != "1":
        raise HTTPException(status_code=403, detail="Not allowed")
    try:
        count = seed_news(db, reset=reset)
    except FileNotFoundError as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
    return schemas.SeedResponse(seeded=count, reset=reset)
