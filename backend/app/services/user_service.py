from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse
from app.core.security import get_password_hash, verify_password


# Create a new user
async def create_user(user_create: UserCreate, db: AsyncSession):
    existing_user = await db.execute(
        select(User).where(User.email == user_create.email)
    )
    if existing_user.scalar_one_or_none():
        return None  # User already exists

    hashed_password = get_password_hash(user_create.password)
    user = User(email=user_create.email, hashed_password=hashed_password)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user


# Authenticate user by verifying credentials
async def authenticate_user(email: str, password: str, db: AsyncSession):
    result = await db.execute(select(User).where(User.email == email))
    user = result.scalar_one_or_none()
    if not user:
        return None  # User not found

    if not verify_password(password, user.hashed_password):
        return None  # Password mismatch

    return user
