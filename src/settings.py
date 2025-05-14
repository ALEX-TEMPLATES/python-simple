from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    dsn: str = "example"

    class Config:
        env_file = "../.env"


settings = Settings()
