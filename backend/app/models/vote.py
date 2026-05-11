from sqlalchemy import Column, Integer, ForeignKey
from app.database import Base

class Vote(Base):
    __tablename__ = "votes"

    id = Column(Integer, primary_key=True, index=True)

    value = Column(Integer)

    user_id = Column(Integer, ForeignKey("users.id"))

    post_id = Column(Integer, ForeignKey("posts.id"))