from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import httpx

templates = Jinja2Templates(directory="app/templates")
router = APIRouter()


@router.get("/signup", response_class=HTMLResponse)
async def signup_page(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})


@router.post("/signup", response_class=HTMLResponse)
async def handle_signup(
    request: Request, email: str = Form(...), password: str = Form(...)
):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://localhost:8000/api/auth/signup",
            json={"email": email, "password": password},
        )
        if response.status_code == 200:
            return RedirectResponse(url="/auth/login", status_code=302)
        return templates.TemplateResponse(
            "signup.html", {"request": request, "error": "User already exists"}
        )
