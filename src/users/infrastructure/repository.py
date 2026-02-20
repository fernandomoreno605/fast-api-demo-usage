from sqlalchemy.orm import Session
from src.users.domain.models import User
from src.users.infrastructure.mappers import user_to_model, user_to_entity
from src.users.infrastructure.models import UserModel

class SQLAlchemyUserRepository():
  def __init__(self, session: Session):
    self.session = session
  
  def get_all(self) -> list[User]:
    models = self.session.query(UserModel).all()
    return [user_to_entity(model) for model in models]
  
  def get_by_id(self, id: int) -> User:
    raise NotImplementedError
  
  def create(self, user: User) -> User:
    model = user_to_model(user)
    self.session.add(model)
    self.session.commit()
    self.session.refresh(model)
    return model
  
  def update(self, user: User) -> User:
    raise NotImplementedError
  
  def delete(self, id: int) -> None:
    raise NotImplementedError