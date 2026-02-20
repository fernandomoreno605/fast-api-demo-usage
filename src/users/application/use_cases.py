from src.users.domain.repository import UserRepository
from src.users.domain.models import User


class UserUseCases:
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
    
    def update_user(self, user_id, user_data):
      return self.user_repository.update(user_id, user_data)
    
    def delete_user(self, user_id):
      return self.user_repository.delete(user_id)