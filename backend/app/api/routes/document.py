from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.core.database import get_db
from app.services.document_service import (
    create_document, get_document_by_id, get_all_documents, delete_document
)
from app.schemas.document import DocumentCreate, DocumentResponse

router = APIRouter()

@router.post("/", response_model=DocumentResponse)
async def create_new_document(
    document: DocumentCreate, db: AsyncSession = Depends(get_db)
):
    return await create_document(db, document.title, document.content, document.owner_id)

@router.get("/{document_id}", response_model=DocumentResponse)
async def get_document(document_id: int, db: AsyncSession = Depends(get_db)):
    document = await get_document_by_id(db, document_id)
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
    return document

@router.get("/", response_model=List[DocumentResponse])
async def list_documents(owner_id: int, db: AsyncSession = Depends(get_db)):
    return await get_all_documents(db, owner_id)

@router.delete("/{document_id}")
async def delete_document_endpoint(document_id: int, db: AsyncSession = Depends(get_db)):
    success = await delete_document(db, document_id)
    if not success:
        raise HTTPException(status_code=404, detail="Document not found")
    return {"message": "Document deleted successfully"}
