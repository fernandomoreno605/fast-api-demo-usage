from fastapi import FastAPI
from src.database import Base, engine
from src.users.infrastructure.routers import router as users_router
from src.posts.infrastructure.routers import router as posts_router

app = FastAPI()
app.title = "Fernando's FastAPI Example usage"
app.version = "1.0.0"
app.description = "This is a simple API made with FastAPI"
app.contact = {
  "name": "Fernando",
  "email": "fernandomoreno605@gmail.com"
}
app.license_info = {
  "name": "MIT",
  "url": "https://opensource.org/licenses/MIT"
}

Base.metadata.create_all(bind=engine)


app.include_router(users_router)
app.include_router(posts_router)

@app.get("/", tags=["Home"], summary="Home page", description="This is the home page of the API")
def home_page():
  return {"message": "Hello World!"}


# @app.get("/users", tags=["Users"], summary="Get all users", description="This is the list of all users")
# def get_users(db: Annotated[Session, Depends(get_db)]):
#   result = db.execute(select(Users).all())
#   return result

# @app.get("/users/{user_id}", tags=["Users"], summary="Get a user by id", description="This is the user with the id")
# def get_user_by_id(user_id: int):
#   user = next((user for user in users if user["id"] == user_id), None)
#   return user if user else {"message": "User not found"}

# @app.get("/users/", tags=["Users"], summary="Get a user by params", description="This is the user with the params")
# def get_user_by_params(name: str = Query(None, description="The name of the user"), age: int = Query(None, description="The age of the user")):
#   users_filtered = users
#   if name is not None:
#     users_filtered = [user for user in users_filtered if user["name"].lower() == name.lower()]
#   if age is not None:
#     users_filtered = [user for user in users_filtered if user["age"] == age]
#   return users_filtered if users_filtered else {"message": "Users not found"}

# @app.post("/users", tags=["Users"], summary="Create a user", description="This is the user with the params")
# def create_user(user: User) -> User:
#   users.append(user.model_dump())
#   print("New users list: ", users)
#   return user