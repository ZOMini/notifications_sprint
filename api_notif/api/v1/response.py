from bson import ObjectId
from pydantic import Field as PydanticField

from api.v1.models import OrJsonModel


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate
    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)
    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class ResponseGetCreateUser(OrJsonModel):
    '''Для GET ручки.'''
    notif_id: PyObjectId  = PydanticField(default_factory=PyObjectId)
    user_id: str
    username: str
    email: str
    status: bool = False

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "notifid": "6400ccf083ea90a98ac45eec",
                "userid": "dadd35b1-7b11-4aa1-a871-61fddb4faa27",
                "username": "Vet",
                "email": "ee-2233@mail.ru",
                "status": False
            }
        }
