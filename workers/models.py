import orjson
from pydantic import UUID4, BaseModel
from enum import Enum
from datetime import datetime


def orjson_dumps(v, *, default):
    return orjson.dumps(v, default=default).decode()


class OrJsonModel(BaseModel):

    class Config:
        json_loads = orjson.loads
        json_dumps = orjson_dumps


class EventTypeEnum(str, Enum):
    user_create = 'user_create'
    change_password = 'change_password'


class InstantNotificationEvent(OrJsonModel):
    user_id: str
    event_type: EventTypeEnum
    datetime: datetime

    class Config:
        schema_extra = {
            "example": {
                "user_id": "dadd35b1-7b11-4aa1-a871-61fddb4faa27",
                "username": "Vet",
                "email": "ee-2233@mail.ru"
            }
        }