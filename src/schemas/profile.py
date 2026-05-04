from pydantic import BaseModel, Field
from uuid import UUID
from typing import Optional

class ProfileCreate(BaseModel):
    user_id: UUID
    name: str

class ProfileUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    profile_picture_url: Optional[str] = None

class ProfilePublicResponse(BaseModel):
    user_id: UUID
    name: str
    description: Optional[str] = None
    profile_picture_url: Optional[str] = None

    class Config:
        from_attributes = True
