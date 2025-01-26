from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.document import Document

async def create_document(db: AsyncSession, title: str, content: str, owner_id: int):
    document = Document(title=title, content=content, owner_id=owner_id)
    db.add(document)
    await db.commit()
    await db.refresh(document)
    return document

async def get_document_by_id(db: AsyncSession, document_id: int):
    result = await db.execute(select(Document).where(Document.id == document_id))
    return result.scalar_one_or_none()

async def get_all_documents(db: AsyncSession, owner_id: int):
    result = await db.execute(select(Document).where(Document.owner_id == owner_id))
    return result.scalars().all()

async def delete_document(db: AsyncSession, document_id: int):
    document = await get_document_by_id(db, document_id)
    if document:
        await db.delete(document)
        await db.commit()
        return True
    return False
