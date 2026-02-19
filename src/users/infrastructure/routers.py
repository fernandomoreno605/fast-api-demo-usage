from fastapi import APIRouter

router = APIRouter(
  prefix="/users",
  tags=["Users"]
)

@router.post("/", summary="Create a user", description="This is the user with the params")
def create_user():
  print("Creating user...")
  return {"message": "User created"}

@router.get("/", summary="Get all users", description="This is the list of all users")
def get_users():
  print("Getting users...")
  return {"message": "Users retrieved"}

@router.get("/{user_id}", summary="Get a user by id", description="This is the user with the id")
def get_user_by_id(user_id: int):
  print("Getting user by id...")
  return {"message": "User retrieved"}

@router.put("/{user_id}", summary="Update a user", description="This is the user with the params")
def update_user(user_id: int):
  print("Updating user...")
  return {"message": "User updated"}

@router.delete("/{user_id}", summary="Delete a user", description="This is the user with the params")
def delete_user(user_id: int):
  print("Deleting user...")
  return {"message": "User deleted"}