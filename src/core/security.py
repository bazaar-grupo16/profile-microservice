from fastapi import Header, HTTPException, status
from uuid import UUID

def get_current_user_id(x_user_id: str = Header(default=None)) -> UUID:
    if not x_user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Falta el header x-user-id. No estás autenticado."
        )
    
    try:
        return UUID(x_user_id)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El formato del x-user-id no es un UUID válido."
        )