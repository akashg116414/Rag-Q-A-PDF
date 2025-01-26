from app.models.document import Document
from app.core.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession

async def ingest_document(title: str, content: str, owner_id: int, db: AsyncSession):
    doc = Document(title=title, content=content, owner_id=owner_id)
    db.add(doc)
    await db.commit()
    await db.refresh(doc)
    return doc
