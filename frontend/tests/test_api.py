import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_signup_page():
    response = client.get("/auth/signup")
    assert response.status_code == 200
    assert "Sign Up" in response.text

def test_user_signup():
    response = client.post("/auth/signup", json={"email": "test@example.com", "password": "password123"})
    assert response.status_code in [200, 400]  # 400 if user already exists

def test_login_page():
    response = client.get("/auth/login")
    assert response.status_code == 200
    assert "Login" in response.text

def test_upload_page():
    response = client.get("/upload")
    assert response.status_code == 200
    assert "Upload PDF Document" in response.text
