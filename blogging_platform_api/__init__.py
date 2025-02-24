from contextlib import asynccontextmanager
from fastapi import FastAPI
from .routes.posts import router as posts_router
from .core.database import create_db_and_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(posts_router)
