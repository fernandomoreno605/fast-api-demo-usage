from sqlalchemy.orm import Session
from src.users.application.services import UserServices
from src.users.infrastructure.repository import SQLAlchemyUserRepository

def get_user_services(session: Session) -> UserServices:
  return UserServices(
    user_repository=SQLAlchemyUserRepository(session=session)
  )