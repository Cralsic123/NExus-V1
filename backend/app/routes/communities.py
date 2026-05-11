from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.community import Community
from app.schemas.community import CommunityCreate

router = APIRouter(prefix="/communities")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_community(
    community: CommunityCreate,
    db: Session = Depends(get_db)
):

    new_community = Community(
        name=community.name,
        description=community.description
    )

    db.add(new_community)

    db.commit()

    db.refresh(new_community)

    return new_community

@router.get("/")
def get_communities(db: Session = Depends(get_db)):

    return db.query(Community).all()