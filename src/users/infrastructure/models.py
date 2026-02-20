from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base
from sqlalchemy.orm import relationship

class UserModel(Base):
  __tablename__ = "users"
  id: Mapped[int] = mapped_column(Integer,primary_key=True, index=True)
  name: Mapped[str] = mapped_column(String(length=255), nullable=False)
  last_name: Mapped[str] = mapped_column(String(length=255), nullable=False)
  username: Mapped[str] = mapped_column(String(length=100), nullable=True, unique=True)
  password: Mapped[str] = mapped_column(String(length=255), nullable=False)
  email: Mapped[str] = mapped_column(String(length=255), nullable=False, unique=True)
  age: Mapped[int] = mapped_column(Integer, nullable=True)

  # posts: Mapped[list["Post"]] = relationship(back_populates="author")