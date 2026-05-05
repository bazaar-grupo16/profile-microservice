from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from uuid import UUID

from src.repositories import profile as profile_repo

def get_my_profile(user_id: UUID, db: Session):
    profile = profile_repo.get_profile_by_user_id(db, user_id=user_id)
    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Perfil no encontrado"
        )
    return profile