#create a schema for the blogs
from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List
from typing import Literal

class Blog(BaseModel):

    unique_link: str
    title: str
    description: str
    content: dict
    author: str
    cover_image: Optional[str]
    thumbnail_image: Optional[str]
    tags: Optional[List[str]]
    status: Optional[Literal["draft", "published"]] = "draft"
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
