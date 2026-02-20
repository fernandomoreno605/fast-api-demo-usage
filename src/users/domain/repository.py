from src.users.domain.models import User

class UserRepository:
    def get_all(self) -> list[User]:
        raise NotImplementedError
    
    def get_by_id(self, id: int) -> User:
        raise NotImplementedError
    
    def create(self, user: User) -> User:
        raise NotImplementedError
    
    def update(self, user: User) -> User:
        raise NotImplementedError
    
    def delete(self, id: int) -> None:
        raise NotImplementedError