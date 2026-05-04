from sqlalchemy import Column, String, DateTime, Uuid
from datetime import datetime, timezone
from src.core.database import Base

class Profile(Base):
    __tablename__ = "profiles"

    user_id = Column(Uuid, primary_key=True, index=True) 
    
    name = Column(String(100), nullable=False)
    description = Column(String(500), nullable=True)
    profile_picture_url = Column(String, nullable=True)
    
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))