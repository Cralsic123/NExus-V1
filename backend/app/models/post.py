from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.database import Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)

    content = Column(Text)

    image = Column(String, nullable=True)

    votes = Column(Integer, default=0)

    user_id = Column(Integer, ForeignKey("users.id"))

    community_id = Column(Integer, ForeignKey("communities.id"))

    created_at = Column(DateTime(timezone=True), server_default=func.now())