from fastapi import APIRouter, Depends, HTTPException
from pydantic import Field

from api.v1.models import RequestPostCreateUser, RequestPostReviewLike
from api.v1.response import ResponseGetCreateUser
from services.notif_serv import NotificationService, get_notif_service

router = APIRouter()
RESP400 = {"detail": "bad request"}
RESP404 = {"detail": "not found"}


@router.post('/create_user', responses={400: RESP400})
async def post_notif_create_user(
    data: RequestPostCreateUser,
    notif_serv: NotificationService = Depends(get_notif_service)) -> None:
    """Постит создание пользователя."""
    await notif_serv.post_notif_create_user(data)


@router.post('/rewiew_like', responses={400: RESP400})
async def post_notif_rewiew_like(
    data: RequestPostReviewLike,
    notif_serv: NotificationService = Depends(get_notif_service)) -> None:
    """Постит лайк ревьюва."""
    await notif_serv.post_notif_review_like(data)


@router.get('/create_user/{user_id}', responses={400: RESP400, 404: RESP404})
async def get_by_userid(
    user_id: str,
    notif_serv: NotificationService = Depends(get_notif_service)) -> list[ResponseGetCreateUser]:
    """Ручка для разработки. Поиск по пользователю.
    Эта ручка может понадобится, а те что ниже удалю после ревью."""
    return await notif_serv._get_by_userid(user_id)


@router.delete('/', responses={400: RESP400})
async def delete_all(
    notif_serv: NotificationService = Depends(get_notif_service)) -> None:
    """Ручка для разработки."""
    await notif_serv._delete_all()


@router.get('/info', responses={400: RESP400})
async def get_info(
    notif_serv: NotificationService = Depends(get_notif_service)):
    """Ручка для разработки. Список коллекций монго.
    А то джанго/джонго там понаделало... - чтоб под рукой было."""
    return await notif_serv._get_info()
