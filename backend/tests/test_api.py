import pytest
from fastapi.testclient import TestClient
from unittest.mock import AsyncMock, MagicMock
from app.main import app

client = TestClient(app)


@pytest.fixture
def mock_db():
    return AsyncMock()


@pytest.fixture
def mock_openai(mocker):
    return mocker.patch("app.api.routes.qa.OpenAIEmbeddings", autospec=True)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "API is running"


def test_upload_pdf(mocker, mock_db):
    mocker.patch(
        "app.utils.pdf_utils.extract_text_from_pdf", return_value="Extracted PDF text"
    )
    mocker.patch("app.api.routes.upload.FAISS.from_texts", return_value=MagicMock())

    file_path = "tests/sample.pdf"
    with open(file_path, "rb") as file:
        response = client.post(
            "/api/upload", files={"file": ("sample.pdf", file, "application/pdf")}
        )

    assert response.status_code == 201
    assert "filename" in response.json()


def test_ask_question(mocker, mock_db, mock_openai):
    mock_retriever = mocker.patch(
        "app.api.routes.qa.FAISS.as_retriever", return_value=MagicMock()
    )
    mock_retriever.return_value.get_relevant_documents.return_value = [
        {"page_content": "Mocked Answer"}
    ]

    mock_faiss = mocker.patch(
        "app.api.routes.qa.FAISS.from_texts", return_value=MagicMock()
    )

    mock_faiss.return_value = MagicMock()
    mock_faiss.return_value.save_local = MagicMock()

    mock_embeddings = mock_openai.return_value.embed_documents.return_value = [
        "mocked_embedding"
    ]

    mock_qa_chain = mocker.patch(
        "app.api.routes.qa.RetrievalQA.from_llm", return_value=MagicMock()
    )
    mock_qa_chain.return_value.run.return_value = "Mocked AI Answer"

    payload = {"document_id": 1, "question": "What is AI?"}
    response = client.post("/api/qa/ask", params=payload)

    assert response.status_code == 200
    assert response.json()["answer"] == "Mocked AI Answer"
