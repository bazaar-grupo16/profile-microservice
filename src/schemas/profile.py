from pydantic import BaseModel
from uuid import UUID
from typing import Optional

class ProfileCreate(BaseModel):
    user_id: UUID
    name: str

class ProfilePrivateResponse(BaseModel):
    user_id: UUID
    name: str
    description: Optional[str] = None
    profile_picture_url: Optional[str] = None

    class Config:
        from_attributes = True

class ProfileUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    profile_picture_url: Optional[str] = None

class ProfilePublicResponse(BaseModel):
    user_id: UUID
    name: str
    description: str | None = None
    profile_picture_url: str | None = None

    class Config:
        from_attributes = True
