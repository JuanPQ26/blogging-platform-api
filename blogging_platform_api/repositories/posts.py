from dataclasses import dataclass
from sqlmodel import Session, select, delete, update
from ..models.post import Post, Tag

@dataclass
class PostsRespository:
    def find_all(self, db: Session) -> list[Post]:
        posts = db.exec(select(Post)).all()
        return posts

    def find_by_id(self, id: int, db: Session) -> Post:
        post = db.exec(select(Post).where(Post.id == id)).first()
        return post

    def save(self, post: Post, db: Session) -> Post:
        db.add(post)
        db.commit()
        db.refresh(post)

        return post

    def delete(self, id: int, db: Session) -> None:
        db.exec(delete(Post).where(Post.id == id))
        db.exec(delete(Tag).where(Tag.post_id == id))
        
        db.commit()
