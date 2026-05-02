import csv
from pathlib import Path

import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = BASE_DIR / "data" / "sample_train.csv"
MODEL_DIR = BASE_DIR / "app" / "models"
MODEL_PATH = MODEL_DIR / "sentiment_model.pkl"


def load_data(path: Path):
    texts = []
    labels = []
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            text = row.get("text")
            label = row.get("label")
            if not text or not label:
                continue
            texts.append(text.strip())
            labels.append(label.strip())
    return texts, labels


def train_model(texts, labels):
    pipeline = Pipeline([
        ("tfidf", TfidfVectorizer(ngram_range=(1, 2), min_df=1)),
        ("clf", LinearSVC())
    ])
    pipeline.fit(texts, labels)
    return pipeline


def main():
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Training data not found: {DATA_PATH}")
    texts, labels = load_data(DATA_PATH)
    if not texts:
        raise ValueError("Training data is empty")
    model = train_model(texts, labels)
    MODEL_DIR.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    print(f"Model saved to {MODEL_PATH}")


if __name__ == "__main__":
    main()
