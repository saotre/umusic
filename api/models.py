import datetime
import uuid

from pydantic import BaseModel, BaseSettings, Field


class User(BaseModel):
    id: uuid.UUID
    name: str
    token: uuid.UUID
    created_at: datetime.datetime


class Audio(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    mp3: bytes
    created_at: datetime.datetime

class PostgresDsn(BaseSettings):
    dbname: str = Field(..., env="DB_NAME")
    user: str = Field(..., env="DB_USER")
    password: str = Field(..., env="DB_PASSWORD")
    host: str = Field(..., env="DB_HOST")
    port: int = Field(..., env="DB_PORT")
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

POSTGRES_DSN = PostgresDsn().dict()
