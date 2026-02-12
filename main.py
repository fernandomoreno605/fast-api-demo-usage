from fastapi import FastAPI, Query
from pydantic import BaseModel
from database import SessionLocal, engine
import models

app = FastAPI()
app.title = "Fernando's First FastAPI API"
app.version = "1.0.0"
app.description = "This is a simple API to learn FastAPI"
app.contact = {
  "name": "Fernando",
  "email": "fernandomoreno605@gmail.com"
}
app.license_info = {
  "name": "MIT",
  "url": "https://opensource.org/licenses/MIT"
}

models.Base.metadata.create_all(bind=engine)

users = [
  {
    "id": 1,
    "name": "Fernando",
    "email": "fernandomoreno605@gmail.com",
    "age": 20
  },
  {
    "id": 2,
    "name": "Juan",
    "email": "juan@example.com",
    "age": 21
  },
  {
    "id": 3,
    "name": "Maria",
    "email": "maria@example.com",
    "age": 22
  },
    {
    "id": 4,
    "name": "Fernando",
    "email": "fernando@example.com",
    "age": 23
  }
]

class User(BaseModel):
  id: int
  name: str
  email: str
  age: int

@app.get("/", tags=["Home"], summary="Home page", description="This is the home page of the API")
def home_page():
  return {"message": "Hello World 2!"}


@app.get("/users", tags=["Users"], summary="Get all users", description="This is the list of all users")
def get_users():
  return users

@app.get("/users/{user_id}", tags=["Users"], summary="Get a user by id", description="This is the user with the id")
def get_user_by_id(user_id: int):
  user = next((user for user in users if user["id"] == user_id), None)
  return user if user else {"message": "User not found"}

@app.get("/users/", tags=["Users"], summary="Get a user by params", description="This is the user with the params")
def get_user_by_params(name: str = Query(None, description="The name of the user"), age: int = Query(None, description="The age of the user")):
  users_filtered = users
  if name is not None:
    users_filtered = [user for user in users_filtered if user["name"].lower() == name.lower()]
  if age is not None:
    users_filtered = [user for user in users_filtered if user["age"] == age]
  return users_filtered if users_filtered else {"message": "Users not found"}

@app.post("/users", tags=["Users"], summary="Create a user", description="This is the user with the params")
def create_user(user: User) -> User:
  users.append(user.model_dump())
  print("New users list: ", users)
  return user