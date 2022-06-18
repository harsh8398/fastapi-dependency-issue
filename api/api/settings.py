import os

from pydantic import BaseSettings, PostgresDsn

SQLALCHEMY_DATABASE_URL = (
    f'postgresql://{os.getenv("POSTGRES_USER")}:{os.getenv("POSTGRES_PASSWORD")}@'
    f'{os.getenv("POSTGRES_HOST")}/{os.getenv("POSTGRES_DB")}'
)


class Settings(BaseSettings):
    pg_dsn: PostgresDsn


settings = Settings(pg_dsn=SQLALCHEMY_DATABASE_URL)
