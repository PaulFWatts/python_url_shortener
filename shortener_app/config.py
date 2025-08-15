# shortener_app/config.py

from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables or .env file.

    Attributes:
        env_name (str): The name of the environment (e.g., Local, Development).
        base_url (str): The base URL for the application.
        db_url (str): The database connection URL.
    """

    env_name: str = "Local"
    base_url: str = "http://localhost:8000"
    db_url: str = "sqlite:///./shortener.db"

    class Config:
        env_file = ".env"


@lru_cache
def get_settings() -> Settings:
    """
    Returns a cached instance of Settings loaded from environment variables or .env file.
    Useful for dependency injection in FastAPI or other frameworks.
    """
    settings = Settings()
    print(f"Loading settings for: {settings.env_name}")
    return settings
