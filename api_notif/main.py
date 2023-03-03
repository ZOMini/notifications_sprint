import logging

import uvicorn
from fastapi import FastAPI, Request, Response
from fastapi.responses import ORJSONResponse

from api.v1 import notification
from core.config import settings
from core.logger import RequestIdFilter, init_logs

app = FastAPI(
    title=f'{settings.module_name}_api',
    debug=settings.debug,
    docs_url='/notif/api/openapi',
    openapi_url='/notif/api/openapi.json',
    default_response_class=ORJSONResponse,
)

app.include_router(notification.router, prefix='/notif/api/v1', tags=['notification'])

@app.on_event('startup')
async def startup():
    init_logs()


@app.middleware("http")
async def add_request_id(request: Request, call_next):
    """Добавление requist id в логгеры. """
    uvicorn_access_logger = logging.getLogger("uvicorn.access")
    uvicorn_access_logger.addFilter(RequestIdFilter(request, 'RequestIdFilter'))
    uvicorn_error_logger = logging.getLogger("uvicorn.error")
    uvicorn_error_logger.addFilter(RequestIdFilter(request, 'RequestIdFilter'))
    response: Response = await call_next(request)
    return response


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8001, limit_max_requests=1024, workers=1, reload=True)
