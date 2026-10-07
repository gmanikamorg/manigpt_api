from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from controllers.auth_controller import AuthController
from core.dependencies import get_db
from schemas.auth import LoginRequest, RegisterRequest, TokenResponse

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/register",
    status_code=status.HTTP_201_CREATED,
)
def register(
    request: RegisterRequest,
    db: Session = Depends(get_db),
):
    controller = AuthController(db)

    user = controller.register(request)

    return {
        "id": user.id,
        "name": user.name,
        "email": user.email,
    }


@router.post(
    "/login",
    response_model=TokenResponse,
)
def login(
    request: LoginRequest,
    db: Session = Depends(get_db),
):
    controller = AuthController(db)

    access_token = controller.login(request)

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }
