from typing import Self
from pydantic import BaseModel, Field
from src.common.infrastructure.shared_schema import APIOutput
from src.users.domain.models import User


class CreateUserInputSchema(BaseModel):
  name: str = Field(..., min_length=1, max_length=100, description="User name")
  last_name: str = Field(..., min_length=1, max_length=100, description="User last name")
  username: str = Field(..., min_length=1, max_length=100, description="User username")
  password: str = Field(..., min_length=1, max_length=100, description="User password")
  email: str = Field(..., min_length=1, max_length=100, description="User email")
  age: int | None = Field(None, ge=0, le=100, description="User age")

class UpdateUserInputSchema(BaseModel):
  name: str | None = Field(None, min_length=1, max_length=100, description="User name")
  last_name: str | None = Field(None, min_length=1, max_length=100, description="User last name")
  password: str | None = Field(None, min_length=1, max_length=100, description="User password")
  email: str | None = Field(None, min_length=1, max_length=100, description="User email")
  age: int | None = Field(None, ge=0, le=100, description="User age")

class UserOutputSchema(APIOutput):
  id: int
  name: str
  last_name: str
  username: str
  email: str
  age: int | None = None

  @classmethod
  def from_entity(cls, entity: User) -> Self:
    return cls(
      id=entity.id,
      name=entity.name,
      last_name=entity.last_name,
      username=entity.username,
      email=entity.email,
      age=entity.age
    )
