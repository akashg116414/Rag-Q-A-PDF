from fastapi import APIRouter, Depends
from app.services.qa_service import generate_answer
from typing import List

router = APIRouter()

@router.post("/")
async def get_answer(question: str, documents: List[str]):
    answer = await generate_answer(question, documents)
    return answer
