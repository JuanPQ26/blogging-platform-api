from sqlmodel import create_engine, SQLModel
from .settings import settings

engine = create_engine(settings.database_url)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)