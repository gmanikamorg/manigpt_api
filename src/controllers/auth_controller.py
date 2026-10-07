from sqlalchemy.orm import Session

from schemas.auth import LoginRequest, RegisterRequest
from services.auth_service import AuthService


class AuthController:

    def __init__(self, db: Session):
        self.auth_service = AuthService(db)

    def register(self, request: RegisterRequest):
        return self.auth_service.register(
            name=request.name,
            email=request.email,
            password=request.password,
        )

    def login(self, request: LoginRequest):
        return self.auth_service.login(
            email=request.email,
            password=request.password,
        )
