from pydantic import BaseModel
from huggingfastapi.core.config import QUESTION_ANSWER_MODEL


class QAPredictionResult(BaseModel):

    score: float
    start: int
    end: int
    answer: str
    model: str = QUESTION_ANSWER_MODEL
