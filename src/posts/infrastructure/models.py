from src.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey

class Post(Base):
  __tablename__ = "posts"
  id: Mapped[int] = mapped_column(Integer,primary_key=True, index=True)
  title: Mapped[str] = mapped_column(String(length=255), nullable=False)
  content: Mapped[str] = mapped_column(String(length=255), nullable=False)
  user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False, index=True)

  author: Mapped["User"] = relationship(back_populates="posts")