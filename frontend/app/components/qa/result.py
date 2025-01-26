from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/templates")
router = APIRouter()

@router.get("/qa/result", response_class=HTMLResponse)
async def result_component(request: Request, question: str, answer: str):
    return templates.TemplateResponse("qa/result.html", {"request": request, "question": question, "answer": answer})
