from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    POSTGRES_HOST: str
    POSTGRES_PORT: str
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    TG_TOKEN: str
    ADMIN: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
