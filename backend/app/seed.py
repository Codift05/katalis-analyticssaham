import csv
from pathlib import Path
import random
from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from . import models

BASE_DIR = Path(__file__).resolve().parents[1]
SEED_PATH = BASE_DIR / "data" / "sample_seed.csv"


def _load_rows(path: Path):
    rows = []
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            if not row.get("title"):
                continue
            rows.append(row)
    return rows


def seed_news(db: Session, reset: bool = False) -> int:
    if not SEED_PATH.exists():
        raise FileNotFoundError(f"Seed file not found: {SEED_PATH}")

    if reset:
        db.query(models.News).delete()
        db.commit()

    existing = db.query(models.News).count()
    if existing > 0 and not reset:
        return 0

    rows = _load_rows(SEED_PATH)
    for row in rows:
        random_minutes = random.randint(0, 24 * 60)
        created = datetime.utcnow() - timedelta(minutes=random_minutes)
        item = models.News(
            source=row.get("source", "Unknown").strip(),
            title=row.get("title", "").strip(),
            sentiment=row.get("sentiment", "Neutral").strip(),
            created_at=created
        )
        db.add(item)
    db.commit()
    return len(rows)
