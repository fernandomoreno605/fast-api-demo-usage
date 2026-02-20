from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.users.application.use_cases import UserUseCases
from src.users.infrastructure.repository import SQLAlchemyUserRepository
from src.users.infrastructure.schemas import CreateUserInputSchema, UserOutputSchema

router = APIRouter(
  prefix="/users",
  tags=["Users"]
)

@router.post("/", summary="Create a user", description="This is the user with the params")
def create_user(user: CreateUserInputSchema , db: Annotated[Session, Depends(get_db)]):
  user_repository = SQLAlchemyUserRepository(session=db)
  use_cases = UserUseCases(user_repository=user_repository)
  result = use_cases.create_user(user.model_dump())
  return {"message": "User created"}

@router.get("/", summary="Get all users", description="This is the list of all users")
def get_users(db: Annotated[Session, Depends(get_db)]):
  user_repository = SQLAlchemyUserRepository(session=db)
  use_cases = UserUseCases(user_repository=user_repository)
  users = use_cases.get_all_users()
  return [UserOutputSchema.from_entity(user) for user in users]

@router.get("/{user_id}", summary="Get a user by id", description="This is the user with the id")
def get_user_by_id(user_id: int):
  print("Getting user by id...")
  return {"message": "User retrieved"}

@router.put("/{user_id}", summary="Update a user", description="This is the user with the params")
def update_user(user_id: int):
  print("Updating user...")
  return {"message": "User updated"}

@router.delete("/{user_id}", summary="Delete a user", description="This is the user with the params")
def delete_user(user_id: int):
  print("Deleting user...")
  return {"message": "User deleted"}