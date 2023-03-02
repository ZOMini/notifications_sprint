from fastapi import APIRouter, Depends, HTTPException
from pydantic import Field

from api.v1.models import RequestPostCreateUser
from api.v1.response import ResponseGetCreateUser
from services.notif_serv import NotificationService, get_notif_service

router = APIRouter()
RESP400 = {"detail": "bad request"}
RESP404 = {"detail": "not found"}


@router.post('/', responses={400: RESP400})
async def post_notif_create_user(
    data: RequestPostCreateUser,
    notif_serv: NotificationService = Depends(get_notif_service)) -> None:
    """Постит создание пользователя."""
    await notif_serv.post_notif_create_user(data)


@router.get('/{user_id}', responses={400: RESP400, 404: RESP404})
async def get_by_userid(
    user_id: str,
    notif_serv: NotificationService = Depends(get_notif_service)) -> list[ResponseGetCreateUser]:
    """Ручка для разработки. Поиск по пользователю."""
    result =  await notif_serv._get_by_userid(user_id)
    return result

@router.delete('/', responses={400: RESP400})
async def delete_all(
    notif_serv: NotificationService = Depends(get_notif_service)) -> None:
    """Ручка для разработки."""
    await notif_serv._delete_all()
