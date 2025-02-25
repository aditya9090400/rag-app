import os
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://user:password@localhost/db_name")
DATABASE_URL = os.getenv("DATABASE_URL")
# breakpoint()
engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def get_db():
    async with async_session() as session:
        yield session
