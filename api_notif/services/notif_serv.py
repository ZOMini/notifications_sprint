from functools import lru_cache

from fastapi import Depends, HTTPException, status
from motor.motor_asyncio import (
    AsyncIOMotorClient,
    AsyncIOMotorCollection,
    AsyncIOMotorDatabase
)

from api.v1.models import RequestPostCreateUser
from api.v1.response import ResponseGetCreateUser
from core.config import settings
from db.mongo import get_aio_motor


class NotificationService():
    def __init__(self, mongo: AsyncIOMotorClient):
        self.mongo = mongo
        self.db: AsyncIOMotorDatabase = self.mongo[settings.mongo_notif_db]
        self.create_user: AsyncIOMotorCollection = self.db.create_user


    async def post_notif_create_user(self, data: RequestPostCreateUser) -> None:
        try:
            await self.create_user.insert_one(data.dict())
        except Exception as e:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, e.args)

    async def _get_by_userid(self, user_id: str) -> dict:
        try:
            pipeline = [{'$match': {'user_id': user_id, 'status': False}},
                        {'$project': {'_id': 1, 'user_id': 1, 'username': 1, 'email': 1, 'status': 1}},]
            res = []
            async for docs in self.create_user.aggregate(pipeline):
                res.append(ResponseGetCreateUser(**docs, notif_id=docs['_id']))
        except Exception as e:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, e.args)
        if not res:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        return res

    async def _delete_all(self) -> None:
        try:
            await self.mongo.drop_database(settings.mongo_notif_db)
        except Exception as e:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, e.args)

@lru_cache()
def get_notif_service(
        mongo_storage: AsyncIOMotorClient = Depends(get_aio_motor),
    ) -> NotificationService:
    return NotificationService(mongo=mongo_storage)
