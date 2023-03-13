import json
import uuid
import enum

from sqlalchemy import BigInteger, Column, DateTime, ForeignKey, String, Table, Enum, JSON, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from db import Base


class NotificationTypesEnum(enum.Enum):
    user_create = "user_create"
    change_password = "user_create"
    new_films = "new_films"
    received_likes = "received_likes"

class Notification(Base):
    __tablename__ = 'notifications'
    __table_args__ = {'extend_existing': True}

    id = Column(UUID(as_uuid=True),
                primary_key=True,
                default=uuid.uuid4,
                unique=True,
                nullable=False)
    notification_type = Column(String, unique=False, nullable=False)
    notification_data = Column(JSON, unique=False, nullable=True)
    status = Column(Boolean, nullable=False)
    user_id = Column(String, nullable=False)

    def __init__(self, user_id: uuid.uuid4(), notification_type: str,
                 notification_data: dict):
        self.user_id = user_id
        self.notification_type = notification_type
        self.notification_data = json.dumps(notification_type) if notification_data else None
        self.status = False



























