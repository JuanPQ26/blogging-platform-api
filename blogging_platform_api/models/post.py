from typing import Optional

from sqlmodel import Field, Relationship, SQLModel


class Post(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    content: str
    category: str
    tags: list["Tag"] = Relationship(back_populates="post")


class Tag(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    post_id: Optional[int] = Field(default=None, foreign_key="post.id")
    post: Optional[Post] = Relationship(back_populates="tags")
