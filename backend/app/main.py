from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine, Base

from app.routes import auth
from app.routes import posts
from app.routes import communities

# import models
from app.models.user import User
from app.models.post import Post
from app.models.community import Community
from app.models.comment import Comment
from app.models.vote import Vote

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(posts.router)
app.include_router(communities.router)

@app.get("/")
def root():
    return {"message": "NEXUS API RUNNING"}