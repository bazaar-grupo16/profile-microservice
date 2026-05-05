from fastapi import APIRouter, Depends
from uuid import UUID

from src.core.dependencies import DbSession
from src.core.security import get_current_user_id
from src.api.controllers import profile as profile_controller
from src.schemas.profile import ProfilePrivateResponse

router = APIRouter(prefix="/profile", tags=["Profile"])

@router.get("/me", response_model=ProfilePrivateResponse)
def get_my_profile(
    db: DbSession, 
    
    current_user_id: UUID = Depends(get_current_user_id) 
):
    return profile_controller.get_my_profile(user_id=current_user_id, db=db)