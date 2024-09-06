from pydantic import BaseModel, Field, HttpUrl
from typing import List, Optional
import uuid

class Link(BaseModel):
    href: HttpUrl
    title: str
    image: Optional[HttpUrl]

class Social(BaseModel):
    href: HttpUrl
    title: str

class Profile(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    avatar: HttpUrl
    links: List[Link]
    socials: List[Social]

    class Config:
        orm_mode = True
