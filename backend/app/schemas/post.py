from pydantic import BaseModel

class PostCreate(BaseModel):
    title: str
    content: str
    community_id: int