from pydantic import BaseModel
from typing import Optional


class DocumentBase(BaseModel):
    title: str
    content: str


class DocumentCreate(DocumentBase):
    owner_id: int


class DocumentResponse(DocumentBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
