import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API is running!"}


def test_upload_pdf():
    file_path = "tests/sample.pdf" 
    with open(file_path, "rb") as file:
        response = client.post("/api/upload", files={"file": ("sample.pdf", file, "application/pdf")})

    assert response.status_code == 201
    assert "document_id" in response.json()

def test_list_documents():
    response = client.get("/api/documents/list")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_ask_question():
    document_id = 1  # Change this based on uploaded documents
    payload = {"document_id": document_id, "question": "summarize pdf?"}
    response = client.post("/api/ask", json=payload)

    assert response.status_code == 200
    assert "answer" in response.json()
