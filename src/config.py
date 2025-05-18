from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    """
        All Application Configuration
    """
    # Api
    API_HTTP_PORT: int    = int(getenv("API_HTTP_PORT", "80"))
    API_HTTP_WORKERS: int = int(getenv("API_HTTP_WORKERS", "1"))

    # Logging
    LOG_LEVEL: str = getenv("LOG_LEVEL", "INFO")

    # Hugging Face
    EMBEDDING_MODEL_NAME: str = getenv("EMBEDDING_MODEL_NAME")
