from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from auth import authentication
from db import models
from db.database import engine
from routers import comment, post, user

app = FastAPI()

app.include_router(authentication.router)
app.include_router(comment.router)
app.include_router(post.router)
app.include_router(user.router)


@app.get("/")
def root():
    return "Hello World!"


models.Base.metadata.create_all(engine)

app.mount("/images", StaticFiles(directory="images"), name="images")
