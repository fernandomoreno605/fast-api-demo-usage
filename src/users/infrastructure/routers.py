from http import HTTPStatus
from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.users.application.services import UserServices
from src.users.infrastructure.repository import SQLAlchemyUserRepository
from src.users.infrastructure.schemas import CreateUserInputSchema, UserOutputSchema, UpdateUserInputSchema
from src.users.infrastructure.shared import CommonContext, handle_errors

router = APIRouter(
  prefix="/users",
  tags=["Users"]
)
@router.post("/", summary="Create a user", description="This is the user with the params")
@handle_errors
def create_user(user: CreateUserInputSchema , db: Annotated[Session, Depends(get_db)]):
  user_repository = SQLAlchemyUserRepository(session=db)
  use_cases = UserServices(user_repository=user_repository)
  created_user = use_cases.create_user(user.model_dump())
  return (
    UserOutputSchema.from_entity(created_user),
    HTTPStatus.CREATED
  )

@router.get("/", summary="Get all users", description="This is the list of all users")
@handle_errors
def get_users(db: Annotated[Session, Depends(get_db)]):
  user_repository = SQLAlchemyUserRepository(session=db)
  use_cases = UserServices(user_repository=user_repository)
  users = use_cases.get_all_users()
  return [UserOutputSchema.from_entity(user) for user in users]

@router.get("/{user_id}", summary="Get a user by id", description="This is the user with the id")
@handle_errors
def get_user_by_id(user_id: int, db: Annotated[Session, Depends(get_db)]):
  user_repository = SQLAlchemyUserRepository(session=db)
  use_cases = UserServices(user_repository=user_repository)
  user = use_cases.get_user(user_id)
  return UserOutputSchema.from_entity(user)

@router.patch("/{user_id}", summary="Update a user", description="This is the user with the params")
@handle_errors
def update_user(user_id: int, user_data: UpdateUserInputSchema, db: Annotated[Session, Depends(get_db)]):
  patch_data = user_data.model_dump(exclude_unset=True)
  user_repository = SQLAlchemyUserRepository(session=db)
  use_cases = UserServices(user_repository=user_repository)
  result = use_cases.update_user(user_id, patch_data)
  return {"message": "User updated"}

@router.delete("/{user_id}", summary="Delete a user", description="This is the user with the params")
@handle_errors
def delete_user(user_id: int, db: Annotated[Session, Depends(get_db)]):
  user_repository = SQLAlchemyUserRepository(session=db)
  use_cases = UserServices(user_repository=user_repository)
  use_cases.delete_user(user_id)
  return {"message": "User deleted"}