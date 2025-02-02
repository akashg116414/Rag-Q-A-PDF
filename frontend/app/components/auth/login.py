from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import httpx

templates = Jinja2Templates(directory="app/templates")
router = APIRouter()


@router.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@router.post("/login", response_class=HTMLResponse)
async def handle_login(
    request: Request, email: str = Form(...), password: str = Form(...)
):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://localhost:8000/api/auth/login",
            json={"email": email, "password": password},
        )
        if response.status_code == 200:
            token = response.json().get("access_token")
            # Save the token in cookies
            response = RedirectResponse(url="/", status_code=302)
            response.set_cookie(key="token", value=token, httponly=True)
            return response
        return templates.TemplateResponse(
            "login.html", {"request": request, "error": "Invalid credentials"}
        )


@router.get("/logout", response_class=RedirectResponse)
async def logout(request: Request):
    # Clear the token from the cookies
    response = RedirectResponse(url="/", status_code=302)
    response.delete_cookie("token")  # Delete the token cookie
    return response
