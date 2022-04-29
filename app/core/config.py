from pydantic import BaseSettings

class Settings(BaseSettings):
    prefix: str = "/first"
    secret_key: str = None

    class Config:
        env_file = ".env"

settings = Settings()