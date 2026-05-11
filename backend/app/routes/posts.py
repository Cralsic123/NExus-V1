from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.post import Post
from app.schemas.post import PostCreate

router = APIRouter(prefix="/posts")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_post(
    post: PostCreate,
    db: Session = Depends(get_db)
):

    new_post = Post(
        title=post.title,
        content=post.content,
        community_id=post.community_id,
        user_id=1
    )

    db.add(new_post)

    db.commit()

    db.refresh(new_post)

    return new_post

@router.get("/")
def get_posts(db: Session = Depends(get_db)):

    posts = db.query(Post).all()

    return posts