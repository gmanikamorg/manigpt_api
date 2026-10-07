from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from core.security import (
    create_access_token,
    hash_password,
    verify_password,
)
from repositories.user_repository import UserRepository


class AuthService:

    def __init__(self, db: Session):
        self.user_repository = UserRepository(db)

    def register(
        self,
        name: str,
        email: str,
        password: str,
    ):
        existing_user = self.user_repository.get_by_email(email)

        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already registered",
            )

        hashed_password = hash_password(password)

        user = self.user_repository.create(
            name=name,
            email=email,
            password=hashed_password,
        )

        return user

    def login(
        self,
        email: str,
        password: str,
    ):
        user = self.user_repository.get_by_email(email)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password",
            )

        if not verify_password(password, user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password",
            )

        access_token = create_access_token(
            {
                "sub": str(user.id),
            }
        )

        return access_token
