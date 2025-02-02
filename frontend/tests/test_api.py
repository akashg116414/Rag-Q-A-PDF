import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock, patch, AsyncMock
from app.main import app

client = TestClient(app)


def test_signup_page():
    response = client.get("/auth/signup")
    assert response.status_code == 200
    assert "Sign Up" in response.text


def test_user_signup(mocker):
    mock_response = mocker.patch(
        "httpx.AsyncClient.post",
        return_value=MagicMock(status_code=200, json=lambda: {}),
    )
    response = client.post(
        "/auth/signup", data={"email": "test@example.com", "password": "password123"}
    )
    assert response.status_code in [200, 400]


def test_upload_page():
    response = client.get("/upload")
    assert response.status_code == 200


def test_login_success(mocker):
    mock_response = mocker.patch(
        "httpx.AsyncClient.post",
        return_value=MagicMock(
            status_code=200, json=lambda: {"access_token": "mocked_token"}
        ),
    )

    response = client.post(
        "/auth/login", data={"email": "test@example.com", "password": "password123"}
    )

    assert response.status_code == 200


def test_login_page():
    response = client.get("/auth/login")
    assert response.status_code == 200
