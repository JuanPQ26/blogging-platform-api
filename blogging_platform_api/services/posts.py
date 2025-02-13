from dataclasses import dataclass
from fastapi import HTTPException, status
from sqlmodel import Session
from ..models.post import Post, Tag
from ..dtos.posts import CreatePost, UpdatePost, PostResponse
from ..repositories.posts import PostsRespository

@dataclass
class PostsServices:
    posts_repository: PostsRespository

    def find_all(self, db: Session) -> list[PostResponse]:
        posts_found = self.posts_repository.find_all(db)
        return posts_found
    
    def find_by_id(self, id: int, db: Session) -> PostResponse:
        post_found = self.posts_repository.find_by_id(id, db)
        
        if not post_found:
            raise HTTPException(status.HTTP_404_NOT_FOUND, detail={"msg": "Post not found", "type": "not found"})

        return post_found
    
    def create(self, create_post: CreatePost, db: Session) -> PostResponse:
        tags = [Tag(name=tag_name) for tag_name in create_post.tags]

        post = Post(**create_post.model_dump(exclude=["tags"]), tags=tags)
        post_created = self.posts_repository.save(post, db)
        
        return post_created
    
    def update(self, id: int, update_post: UpdatePost, db: Session) -> PostResponse:
        post_found = self.posts_repository.find_by_id(id, db)

        if not post_found:
            raise HTTPException(status.HTTP_404_NOT_FOUND, detail={"msg": "Post not found", "type": "not found"})

        update_post_data = update_post.model_dump(exclude_unset=True, exclude_none=True)

        for key, value in update_post_data.items():
            setattr(post_found, key, value)

        post_updated = self.posts_repository.save(post_found, db)

        return post_updated
    
    def delete(self, id: int, db: Session) -> None:
        self.posts_repository.delete(id, db)
    