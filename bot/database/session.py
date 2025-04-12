from sqlalchemy.ext.asyncio import create_async_engine , async_sessionmaker
from config import config , BASE_DIR
from database.base import Base

engine = create_async_engine(f"sqlite+aiosqlite:///{BASE_DIR}/{config.DB_URL}")

new_session = async_sessionmaker(engine,expire_on_commit=False)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
