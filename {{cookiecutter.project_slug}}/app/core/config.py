from pydantic import BaseSettings

class Settings(BaseSettings):
    project_name: str = "FastAPI Project"
    version: str = "1.0.0"

    class Config:
        env_file = ".env"

settings = Settings()
