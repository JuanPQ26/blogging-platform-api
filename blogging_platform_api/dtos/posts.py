from typing import Optional
from pydantic import BaseModel

class TagResponse(BaseModel):
    name: str

class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    category: str
    tags: list["TagResponse"]

class CreatePost(BaseModel):
    title: str
    content: str
    category: str
    tags: list[str]

class UpdatePost(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    category: Optional[str] = None
    tags: Optional[list[str]] = None
class CreatePostResponse(BaseModel):
    msg: str = "Post created successfully"
    data: PostResponse

class GetPostsResponse(BaseModel):
    msg: str = "Posts found",
    data: list[PostResponse]

class GetPostResponse(BaseModel):
    msg: str = "Post found"
    data: PostResponse

class UpdatePostResponse(BaseModel):
    msg: str = "Post updated successfully"
    data: PostResponse

class DeletePostResponse(BaseModel):
    msg: str = "Post deleted successfully"
    data: None = None