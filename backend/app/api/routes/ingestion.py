from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.services.ingestion_service import ingest_document

router = APIRouter()

@router.post("/")
async def ingest(title: str, content: str, owner_id: int, db: AsyncSession = Depends(get_db)):
    try:
        doc = await ingest_document(title, content, owner_id, db)
        return {"status": "success", "document": {"id": doc.id, "title": doc.title}}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Ingestion failed: {str(e)}")
