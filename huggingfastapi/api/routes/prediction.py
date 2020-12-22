from fastapi import APIRouter, Depends
from starlette.requests import Request

from huggingfastapi.core import security
from huggingfastapi.models.payload import QAPredictionPayload
from huggingfastapi.models.prediction import QAPredictionResult
from huggingfastapi.services.nlp import QAModel

router = APIRouter()


@router.post("/question", response_model=QAPredictionResult, name="question")
def post_question(
    request: Request,
    authenticated: bool = Depends(security.validate_request),
    block_data: QAPredictionPayload = None,
) -> QAPredictionResult:
    """
    #### Retrieves an answer from context given a question

    """

    model: QAModel = request.app.state.model
    prediction: QAPredictionResult = model.predict(block_data)

    return prediction
