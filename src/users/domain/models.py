from typing import Tuple
from pydantic import BaseModel
from datetime import datetime

from users.domain.events import UserCreated, UserEvents


class User(BaseModel):
  id: int | None = None
  name: str
  last_name: str
  username: str
  password: str
  email: str
  age: int | None = None
  posts: list | None = None

  @classmethod
  def create(
    cls,
    /,
    name: str,
    last_name: str,
    username: str,
    password: str,
    email: str,
    age: int | None = None,
    posts: list | None = None,
  ) -> Tuple["User", list[UserEvents]]:
    user = cls(
      name=name,
      last_name=last_name,
      username=username,
      password=password,
      email=email,
      age=age,
      posts=posts,
    )
    event = UserCreated(
      created_at=datetime.now().isoformat(),
      username=username,
      email=email,
    )
    return user, [event]