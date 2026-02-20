from src.users.domain.models import User
from src.users.infrastructure.models import UserModel

def user_to_model(user: User) -> UserModel:
    return UserModel(
        id=user.id if user.id else None,
        name=user.name,
        last_name=user.last_name,
        username=user.username,
        password=user.password,
        email=user.email,
        age=user.age,
    )

def user_to_entity(model: UserModel) -> User:
    return User(
        id=model.id,
        name=model.name,
        last_name=model.last_name,
        username=model.username,
        password=model.password,
        email=model.email,
        age=model.age,
    )