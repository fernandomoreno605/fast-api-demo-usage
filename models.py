from datetime import datetime
from typing import Type
from uuid import uuid4
from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import UUID, DateTime

Base: Type = declarative_base()

class BaseModel(Base):
  __abstract__ = True
  id: int = Column(UUID, primary_key=True, default=uuid4)
  created_at: datetime = Column(DateTime, default=datetime.now)
  updated_at: datetime = Column(DateTime, default=datetime.now, onupdate=datetime.now)