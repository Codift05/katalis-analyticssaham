from sqlalchemy.orm import Session

from . import models, schemas


def get_news(db: Session, limit: int = 50):
    return db.query(models.News).order_by(models.News.created_at.desc()).limit(limit).all()


def create_news(db: Session, payload: schemas.NewsCreate):
    item = models.News(
        source=payload.source,
        title=payload.title,
        sentiment=payload.sentiment
    )
    db.add(item)
    db.commit()
    db.refresh(item)
    return item
