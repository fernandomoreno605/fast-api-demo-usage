from src.users.domain.repository import UserRepository
from src.users.domain.models import User


class UserServices:
    def __init__(self, user_repository: UserRepository):
      self.user_repository = user_repository
    
    def create_user(self, user_data):
      user, events = User.create(**user_data)
      print("events generated:", events)
      return self.user_repository.create(user)
    
    def get_user(self, user_id):
      return self.user_repository.get_by_id(user_id)
    
    def get_all_users(self):
      return self.user_repository.get_all()
    
    def update_user(self, user_id: int, new_user_data):
      found_user = self.user_repository.get_by_id(user_id)
      if found_user is None:
        raise ValueError(f"User with id {user_id} not found")
      for field, value in new_user_data.items():
        if hasattr(found_user, field):
          setattr(found_user, field, value)
      return self.user_repository.update(found_user)
    
    def delete_user(self, user_id):   
      return self.user_repository.delete(user_id)