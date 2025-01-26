from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user import UserCreate, UserResponse, LoginRequest
from app.services.user_service import create_user, authenticate_user
from app.core.security import create_access_token, get_password_hash
from app.core.database import get_db

router = APIRouter()

@router.post("/signup", response_model=UserResponse)
async def signup(user: UserCreate, db: AsyncSession = Depends(get_db)):
    user_exists = await create_user(user, db)
    if not user_exists:
        raise HTTPException(status_code=400, detail="User already exists")
    return user_exists

@router.post("/login")
async def login(login_request: LoginRequest, db: AsyncSession = Depends(get_db)):
    user = await authenticate_user(login_request.email, login_request.password, db)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    access_token = create_access_token({"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}