import uvicorn

from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.database import Base, db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield


app = FastAPI(lifespan=lifespan)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
