from fastapi import APIRouter

router = APIRouter(
  prefix="/posts",
  tags=["Posts"]
)

@router.get("/", summary="Get all posts", description="This is the list of all posts")
def get_posts():
  print("Getting posts...")
  return {"message": "Posts retrieved"}

@router.get("/{post_id}", summary="Get a post by id", description="This is the post with the id")
def get_post_by_id(post_id: int):
  print("Getting post by id...")
  return {"message": "Post retrieved"}

@router.post("/", summary="Create a post", description="This is the post with the params")
def create_post():
  print("Creating post...")
  return {"message": "Post created"}

@router.put("/{post_id}", summary="Update a post", description="This is the post with the params")
def update_post(post_id: int):
  print("Updating post...")
  return {"message": "Post updated"}

@router.delete("/{post_id}", summary="Delete a post", description="This is the post with the params")
def delete_post(post_id: int):
  print("Deleting post...")
  return {"message": "Post deleted"}