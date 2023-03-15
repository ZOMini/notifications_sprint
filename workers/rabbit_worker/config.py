from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    POSTGRES_DB = Field("notif_db")
    POSTGRES_USER = Field("app")
    POSTGRES_PASSWORD = Field("123qwe")
    POSTGRES_HOST = Field("127.0.0.1")
    DB_DOCKER_HOST = Field("notif_db")
    POSTGRES_PORT = Field("5432")

    SMTP_HOST = Field("smtp.mail.ru")
    SMTP_PORT = Field("465")
    SMTP_USER = Field("cx-1")
    SMTP_PASSWORD = Field("GdnxAjVgycF94ufricER")

    EXCHANGE = Field('notifications')
    INSTANT_QUEUE = Field('instant_events')
    RABBIT_USER = Field('consumer')
    RABBIT_PASS = Field('qweqwe')
    RABBIT_HOST = Field('localhost')

    class Config:
        env_file = '../.env'
        env_file_encoding = 'utf-8'

settings = Settings()
