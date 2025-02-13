from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlmodel import Session
from ..dependencies import get_db, get_posts_service
from ..dtos.posts import CreatePost, UpdatePost, CreatePostResponse, UpdatePostResponse, DeletePostResponse, GetPostsResponse, GetPostResponse
from ..services.posts import PostsServices

router = APIRouter(prefix="/posts")

@router.get("")
def get_posts(
    posts_service: PostsServices = Depends(get_posts_service), 
    db: Session = Depends(get_db)
) -> GetPostsResponse:
    posts = posts_service.find_all(db)

    return {
        "msg": "Posts found",
        "data": posts
    }

@router.get("/{id}")
def get_post(
    id: int,
    posts_service: PostsServices = Depends(get_posts_service),
    db: Session = Depends(get_db)    
) -> GetPostResponse:
    post_found = posts_service.find_by_id(id, db)

    return {
        "msg": "Post found", 
        "data": post_found
    }

@router.post("", status_code=status.HTTP_201_CREATED)
def create_post(
    post: CreatePost,
    posts_service: PostsServices = Depends(get_posts_service),
    db: Session = Depends(get_db)
) -> CreatePostResponse:
    post_created = posts_service.create(post, db)

    return {
        "msg": "Post created successfully",
        "data": post_created
    }

@router.patch("/{id}")
def update_post(
    id: int,
    update_post: UpdatePost,
    posts_service: PostsServices = Depends(get_posts_service),
    db: Session = Depends(get_db)
) -> UpdatePostResponse:
    post_updated = posts_service.update(id, update_post, db)

    return {
        "msg": "Post updated successfully",
        "data": post_updated
    }

@router.delete("/{id}")
def delete_post(
    id: int,
    posts_service: PostsServices = Depends(get_posts_service),
    db: Session = Depends(get_db)
) -> DeletePostResponse:
    posts_service.delete(id, db)

    return {
        "msg": "Post deleted successfully",
        "data": None
    }
