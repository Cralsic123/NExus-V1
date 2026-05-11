from pydantic import BaseModel

class CommunityCreate(BaseModel):
    name: str
    description: str