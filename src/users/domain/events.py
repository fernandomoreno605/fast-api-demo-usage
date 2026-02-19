from dataclasses import dataclass
from src.common.domain.bus.types import Event

@dataclass
class UserCreated(Event):
  username: str
  email: str
  created_at: str

@dataclass
class UserUpdated(Event):
  username: str
  email: str
  updated_at: str

@dataclass
class UserDeleted(Event):
  username: str
  email: str
  deleted_at: str


UserEvents = UserCreated | UserUpdated | UserDeleted