from pydantic import BaseModel


class QAPredictionPayload(BaseModel):

    context: str = "42 is the answer to life, the universe and everything."
    question: str = "What is the answer to life?"
