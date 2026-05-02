from typing import List
from pydantic import BaseModel, Field


class NewsBase(BaseModel):
    source: str = Field(..., min_length=2)
    title: str = Field(..., min_length=4)
    sentiment: str = Field(..., min_length=4)


class NewsCreate(NewsBase):
    pass


class NewsRead(NewsBase):
    id: int

    class Config:
        from_attributes = True


class SentimentRequest(BaseModel):
    texts: List[str] = Field(..., min_items=1)


class SentimentResponse(BaseModel):
    labels: List[str]
