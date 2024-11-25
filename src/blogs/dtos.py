from pydantic import BaseModel
from typing import Optional, List   
from pydantic import RootModel
from typing import Literal
class BlogDto(BaseModel):
    title: str
    description: str
    content: dict
    author: str
    cover_image: Optional[str]
    thumbnail_image: Optional[str]
    tags: Optional[List[str]]


class UpdateBlogDto(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    content: Optional[dict] = None
    cover_image: Optional[str] = None
    thumbnail_image: Optional[str] = None
    status: Optional[Literal["draft", "published"]] = None
    tags: Optional[List[str]] = None

class BlogResponse(BaseModel):
    _id: str
    title: str
    description: str
    author: str
    content: dict
    cover_image: Optional[str]
    thumbnail_image: Optional[str]
    tags: Optional[List[str]]
    status: Optional[Literal["draft", "published"]]
    unique_link: str
    created_at: str
    updated_at: str

class BlogListResponse(RootModel):
    root: list[BlogResponse]

