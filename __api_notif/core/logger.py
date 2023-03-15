import logging

import logstash
from fastapi import Request

from core.config import settings


class RequestIdFilter(logging.Filter):
    def __init__(self, request: Request, name: str):
        self.request = request
        self.name = name
    
    def filter(self, record):
        record.request_id = self.request.headers.get('X-Request-Id')
        record.tags = ['notif-api']
        record.scope = ''
        return True


def init_logs() -> None:
    """Для логирования во всех вариантах запуска."""
    uvicorn_access_logger = logging.getLogger("uvicorn.access")
    if settings.ext_logging:
        logstash_handler = logstash.LogstashHandler(settings.logstash_host, int(settings.logstash_port), version=1)
        uvicorn_access_logger.setLevel(settings.log_level)
        uvicorn_access_logger.addHandler(logstash_handler)
    else:
        uvicorn_access_logger.setLevel(settings.log_level)
        ch = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s - %(module)s - %(funcName)s - line:%(lineno)d - %(levelname)s - %(message)s"
        )
        ch.setFormatter(formatter)
        uvicorn_access_logger.addHandler(ch)
