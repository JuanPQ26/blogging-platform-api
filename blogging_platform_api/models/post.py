from sqlmodel import SQLModel, Field, Relationship

class Post(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    content: str
    category: str
    tags: list["Tag"] = Relationship(back_populates="post") 

class Tag(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    post_id: int | None = Field(default=None, foreign_key="post.id")
    post: Post | None = Relationship(back_populates="tags")
