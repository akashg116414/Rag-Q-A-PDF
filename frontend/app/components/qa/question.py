from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/templates")
router = APIRouter()

@router.get("/qa/question", response_class=HTMLResponse)
async def question_component(request: Request):
    return templates.TemplateResponse("qa/question.html", {"request": request})
