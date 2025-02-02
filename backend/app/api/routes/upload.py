from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
import shutil
import os
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.models.document import Document
from app.utils.pdf_utils import extract_text_from_pdf
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

router = APIRouter(tags=["Upload Documents"])

UPLOAD_FOLDER = "uploaded_pdfs"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/upload", status_code=201)
async def upload_pdf(file: UploadFile = File(...), db: AsyncSession = Depends(get_db)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    # Save file locally
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Save file metadata in SQLite
    document = Document(filename=file.filename, path=file_path)
    db.add(document)
    await db.commit()
    await db.refresh(document)

    # # Extract text & generate embeddings
    # text_content = extract_text_from_pdf(file_path)
    # embeddings = OpenAIEmbeddings()

    # # Store embeddings in FAISS
    # vector_store = FAISS.from_texts([text_content], embeddings)
    # vector_store.save_local("vector_db/")

    return {"message": "File uploaded successfully", "filename": document.filename}
