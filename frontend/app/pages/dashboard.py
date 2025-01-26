from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.api.api_client import fetch_dashboard_data

templates = Jinja2Templates(directory="app/templates")
router = APIRouter()

@router.get("/dashboard", response_class=HTMLResponse)
async def dashboard_page(request: Request):
    documents = await fetch_dashboard_data()  # Fetch documents via API client
    return templates.TemplateResponse("dashboard.html", {"request": request, "documents": documents})
