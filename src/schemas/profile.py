from pydantic import BaseModel, Field
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
