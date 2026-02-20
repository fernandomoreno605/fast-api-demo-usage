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
    model = self.session.get(UserModel, id)
    if model is None:
      raise ValueError(f"User with id {id} not found")
    return user_to_entity(model)
  
  def create(self, user: User) -> User:
    model = user_to_model(user)
    self.session.add(model)
    self.session.commit()
    return model
  
  def update(self, user: User) -> User:
    model = self.session.get(UserModel, user.id)
    if model is None:
      raise ValueError(f"User with id {user.id} not found")

    update_data = user.model_dump(exclude_unset=True, exclude={"id", "posts"})
    for field, value in update_data.items():
      setattr(model, field, value)

    self.session.commit()
    return user_to_entity(model)
  
  def delete(self, id: int) -> None:
    model = self.session.get(UserModel, id)
    if model is None:
      raise ValueError(f"User with id {id} not found")
    self.session.delete(model)
    self.session.commit()
    return None