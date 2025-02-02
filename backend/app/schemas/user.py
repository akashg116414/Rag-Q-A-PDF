from pydantic import BaseModel, EmailStr
from typing import Optional


# Base schema for users
class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str  # For user registration


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class UserResponse(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True  # Enables interaction with ORM objects
