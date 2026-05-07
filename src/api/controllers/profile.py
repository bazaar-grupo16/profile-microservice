from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from uuid import UUID

from src.repositories import profile as profile_repo
from src.schemas.profile import ProfileCreate, ProfileUpdate

def get_my_profile(user_id: UUID, db: Session):
    profile = profile_repo.get_profile_by_user_id(db, user_id=user_id)
    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Perfil no encontrado"
        )
    return profile

def create_profile(profile_in: ProfileCreate, db: Session):
    existing_profile = profile_repo.get_profile_by_user_id(db, user_id=profile_in.user_id)
    if existing_profile:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El perfil para este usuario ya existe."
        )

    return profile_repo.create_profile(db, profile_in=profile_in)

def update_my_profile(user_id: UUID, profile_in: ProfileUpdate, db: Session):
    db_profile = profile_repo.get_profile_by_user_id(db, user_id=user_id)
    
    if not db_profile:
        raise HTTPException(status_code=404, detail="Profile not found")

    update_data = profile_in.model_dump(exclude_unset=True)
    
    return profile_repo.update(db, db_obj=db_profile, obj_in=update_data)