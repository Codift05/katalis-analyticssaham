from app.database import SessionLocal, engine
from app import models
from app.seed import seed_news


def main():
    models.Base.metadata.create_all(bind=engine)
    with SessionLocal() as session:
        count = seed_news(session, reset=True)
    if count == 0:
        print("Seed skipped: data already exists")
    else:
        print(f"Seeded {count} rows into SQLite")


if __name__ == "__main__":
    main()
