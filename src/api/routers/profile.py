from fastapi import APIRouter, Depends, Header, UploadFile, File
from uuid import UUID
from src.core.dependencies import DbSession
#from src.core.security import get_current_user_id
from src.api.controllers import profile as profile_controller
from src.schemas.profile import ProfilePrivateResponse, ProfileCreate, ProfileUpdate
from typing import Annotated

router = APIRouter(prefix="/profile", tags=["Profile"])

@router.get("/me", response_model=ProfilePrivateResponse)
def get_my_profile(
    db: DbSession, 
    
    #current_user_id: UUID = Depends(get_current_user_id) 
    x_user_id: UUID = Header(..., alias="x-user-id")
):
    print(f"DEBUG: El header x-user-id recibido es: '{x_user_id}'")
    
    if not x_user_id:
        from fastapi import HTTPException
        raise HTTPException(status_code=422, detail="El header x-user-id no llegó al servidor")
    #return profile_controller.get_my_profile(user_id=current_user_id, db=db)
    return profile_controller.get_my_profile(user_id=x_user_id, db=db)

@router.post("/", response_model=ProfilePrivateResponse, status_code=201)
def create_profile(
    profile_in: ProfileCreate,
    db: DbSession
):
    return profile_controller.create_profile(profile_in=profile_in, db=db)

@router.patch("/me", response_model=ProfilePrivateResponse)
def update_my_profile(
    profile_in: ProfileUpdate,
    db: DbSession,
    x_user_id: UUID = Header(..., alias="x-user-id")
    #current_user_id: UUID = Depends(get_current_user_id)
):
    return profile_controller.update_my_profile(
        user_id=x_user_id, 
        profile_in=profile_in, 
        db=db
    )

@router.post("/upload-avatar")
async def upload_avatar_endpoint(
    #current_user_id: UUID = Depends(get_current_user_id)
    x_user_id: Annotated[UUID, Header(alias="x-user-id")],
    file: Annotated[UploadFile, File(description="Avatar image file")],
):
    return await profile_controller.upload_avatar(user_id=x_user_id, file=file)