import pytest
from starlette.config import environ
from starlette.testclient import TestClient


environ["API_KEY"] = "72c8e5a5-bb07-4c35-8115-f0c4c60eb790"
environ["DEFAULT_MODEL_PATH"] = "./ml_model/model.pkl"


from huggingfastapi.main import get_app  # noqa: E402


@pytest.fixture()
def test_client():
    app = get_app()
    with TestClient(app) as test_client:
        yield test_client
