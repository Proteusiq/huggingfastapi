from huggingfastapi.core import config


def test_prediction(test_client) -> None:
    response = test_client.post(
        "/api/model/predict",
        json={"text": "hello world!", "model_version": "0.1.0"},
        headers={"token": str(config.API_KEY)},
    )
    assert response.status_code == 200
    assert "model_version" in response.json()


def test_prediction_nopayload(test_client) -> None:
    response = test_client.post(
        "/api/model/predict", json={}, headers={"token": str(config.API_KEY)}
    )
    assert response.status_code == 422
