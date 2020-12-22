import pytest

from huggingfastapi.core import config
from huggingfastapi.models.payload import QAPredictionPayload
from huggingfastapi.models.prediction import QAPredictionResult
from huggingfastapi.services.models import QAModel


def test_prediction(test_client) -> None:
    model_path = config.DEFAULT_MODEL_PATH
    tpp = QAPredictionPayload.parse_obj(
        {"text": "hello world!", "model_version": "0.1.0"}
    )

    tm = QAModel(model_path)
    result = tm.predict(tpp)
    assert isinstance(result, QAPredictionResult)


def test_prediction_no_payload(test_client) -> None:
    model_path = config.DEFAULT_MODEL_PATH

    tm = QAModel(model_path)
    with pytest.raises(ValueError):
        result = tm.predict(None)
        assert isinstance(result, QAPredictionResult)
