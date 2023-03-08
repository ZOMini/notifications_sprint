import uuid

import orjson
from pydantic import UUID4, BaseModel


def orjson_dumps(v, *, default):
    return orjson.dumps(v, default=default).decode()


class OrJsonModel(BaseModel):

    class Config:
        json_loads = orjson.loads
        json_dumps = orjson_dumps


class RequestPostCreateUser(OrJsonModel):
    '''Так как при регистрации уже есть все данные, то проще их передать сразу,
    чтоб не грузить AUTH модуль.'''
    user_id: str
    username: str
    email: str
    status: bool = False

    class Config:
        schema_extra = {
            "example": {
                "user_id": "dadd35b1-7b11-4aa1-a871-61fddb4faa27",
                "username": "Vet",
                "email": "ee-2233@mail.ru"
            }
        }


class RequestPostReviewLike(OrJsonModel):
    '''Сначала только id, по приходу на ручку остальное или в воркере...'''
    user_id: str
    username: str = ""
    email: str = ""
    ready: bool = False
    status: bool = False

    class Config:
        schema_extra = {
            "example": {
                "user_id": "dadd35b1-7b11-4aa1-a871-61fddb4faa27"
            }
        }
