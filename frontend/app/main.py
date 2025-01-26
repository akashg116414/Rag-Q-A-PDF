from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from starlette.middleware.base import BaseHTTPMiddleware

# Import routers
from app.pages.home import router as home_router
from app.pages.dashboard import router as dashboard_router
from app.pages.qa import router as qa_router
from app.pages.upload import router as upload_router
from app.components.auth.login import router as login_router
from app.components.auth.signup import router as signup_router

app = FastAPI(title="Document Q&A Frontend")

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")

# Authentication Middleware
class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Public routes that don't require authentication
        public_routes = ["/auth/login", "/auth/signup", "/static"]

        # Allow requests to public routes
        if any([request.url.path.startswith(route) for route in public_routes]):
            return await call_next(request)

        # Check for token in cookies
        token = request.cookies.get("token")
        if not token:
            return RedirectResponse(url="/auth/login")

        return await call_next(request)

app.add_middleware(AuthMiddleware)

# Include routers
app.include_router(home_router, prefix="")
app.include_router(dashboard_router, prefix="")
app.include_router(qa_router, prefix="")
app.include_router(upload_router, prefix="")
app.include_router(login_router, prefix="/auth")
app.include_router(signup_router, prefix="/auth")
