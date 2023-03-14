from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    POSTGRES_DB = "auth_db"
    POSTGRES_USER = "app"
    POSTGRES_PASSWORD = "123qwe"
    POSTGRES_HOST = "127.0.0.1"
    DB_DOCKER_HOST = "auth_db"
    POSTGRES_PORT = "5432"

    SMTP_HOST = "smtp.mail.ru"
    SMTP_PORT = "465"
    SMTP_USER =
    SMTP_PASSWORD =

    EXCHANGE = 'notifications'
    INSTANT_QUEUE = 'instant_events'
    HOST = 'localhost'
    RABBIT_USER = 'consumer'
    RABBIT_PASS = 'qweqwe'
    RABBIT_HOST = 'localhost'

    class Config:
        env_file = './.env'
        env_file_encoding = 'utf-8'

settings = Settings()
