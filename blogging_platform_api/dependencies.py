from fastapi import Depends
from sqlmodel import Session
from .core.database import engine
from .repositories.posts import PostsRespository
from .services.posts import PostsServices

def get_db():
    with Session(engine) as session:
        yield session

def get_posts_repository() -> PostsRespository:
    return PostsRespository()

def get_posts_service(
    posts_repo: PostsRespository = Depends(get_posts_repository),
) -> PostsServices:
    return PostsServices(posts_repo)
