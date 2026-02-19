from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from config import settings

engine = create_engine(
  settings.DATABASE_URL,
  echo=True,
  pool_pre_ping=True,
  pool_size=10,
  max_overflow=20,
  logging_name="sqlalchemy.engine",
)

SessionLocal = sessionmaker(
  autocommit=False,
  autoflush=False,
  bind=engine
)

class Base(DeclarativeBase):
  __abstract__ = True

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()