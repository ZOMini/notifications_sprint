import os

from pydantic import BaseSettings, Field

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Settings(BaseSettings):
    project_name: str = Field(...)
    debug: bool = Field(False)
    develop: bool = Field(False)
    log_level: str = Field('INFO')
    ext_logging: bool = Field(False)
    logstash_host: str = Field('logstash')
    logstash_port: int = Field(5044)
    mongo_notif_db: str= Field(...)
    mongo_notif_url: str = Field(...)

    class Config:
        env_file = '../.env'

settings = Settings()
if settings.develop:
    settings.mongo_notif_url = 'mongodb://127.0.0.1:27017'
