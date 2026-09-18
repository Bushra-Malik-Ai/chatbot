from datetime import datetime
from pydantic import BaseModel, EmailStr


class UserOut(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    city: str

    class Config:
        from_attributes = True


class LoginRequest(BaseModel):
    email: EmailStr


class LoginResponse(BaseModel):
    success: bool
    message: str
    access_token: str | None = None
    admin_email: str | None = None


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    success: bool
    reply: str


class AuditEntryOut(BaseModel):
    id: int
    actor_email: str
    message: str
    success: bool
    result: str
    created_at: datetime | None = None

    class Config:
        from_attributes = True
