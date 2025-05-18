import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager

from api import router
from config import Config
from huggingface import Embedder


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.embedder = Embedder(
        name = Config.EMBEDDING_MODEL_NAME,
    )
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router)


if __name__ == "__main__":

    uvicorn.run(
        app       = "main:app",
        host      = "0.0.0.0",
        port      = Config.API_HTTP_PORT,
        workers   = Config.API_HTTP_WORKERS,
        log_level = Config.LOG_LEVEL,
    )
