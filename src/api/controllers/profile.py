from fastapi import HTTPException, status, UploadFile
from sqlalchemy.orm import Session
from uuid import UUID

from src.repositories import profile as profile_repo
from src.schemas.profile import ProfileCreate, ProfileUpdate
from src.services.storage import StorageService, ALLOWED_MIME_TYPES, MAX_FILE_SIZE

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

async def upload_avatar(user_id: UUID, file: UploadFile):
    if file.content_type not in ALLOWED_MIME_TYPES:
        raise HTTPException(status_code=400, detail="Formato no soportado.")
    
    file_bytes = await file.read()
    
    if len(file_bytes) > MAX_FILE_SIZE:
        raise HTTPException(status_code=400, detail="La imagen es demasiado pesada.")

    storage = StorageService()
    ext = storage.ext_for(file.content_type)
    nombre_archivo = file.filename if file.filename else f"avatar{ext}"
    key = f"profiles/{user_id}/{nombre_archivo}"
    
    url = storage.upload(data=file_bytes, key=key, content_type=file.content_type)
    
    return {"url": url}