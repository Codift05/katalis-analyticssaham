from typing import List
import joblib

MODEL_PATH = "app/models/sentiment_model.pkl"


class SentimentModel:
    def __init__(self):
        self.model = None

    def load(self):
        self.model = joblib.load(MODEL_PATH)

    def predict(self, texts: List[str]) -> List[str]:
        if self.model is None:
            raise RuntimeError("Model not loaded")
        return [str(label) for label in self.model.predict(texts)]
