from sqlalchemy.orm import Session
from uuid import UUID
from src.models.profile import Profile
from src.schemas.profile import ProfileCreate

def get_profile_by_user_id(db: Session, user_id: UUID) -> Profile | None:
    return db.query(Profile).filter(Profile.user_id == user_id).first()

def create_profile(db: Session, profile_in: ProfileCreate) -> Profile:
    db_profile = Profile(
        user_id=profile_in.user_id,
        name=profile_in.name
    )
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile

def update(db: Session, db_obj: Profile, obj_in: dict):
    for field in obj_in:
        if hasattr(db_obj, field):
            setattr(db_obj, field, obj_in[field])
    
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj
