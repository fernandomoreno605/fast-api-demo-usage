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