import pika
from models import InstantNotificationEvent, EventTypeEnum
from db_models import Notification
from db import db_session
from db import init_db
from mail_sender import send_mail
from config import settings as SETT

credentials = pika.PlainCredentials(username=SETT.RABBIT_USER, password=SETT.RABBIT_PASS)

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=SETT.RABBIT_HOST, credentials=credentials))
channel = connection.channel()
channel.queue_bind(exchange=SETT.EXCHANGE, queue=SETT.INSTANT_QUEUE)


def callback(ch, method, properties, body):

    notification = InstantNotificationEvent.parse_raw(body)
    if notification.event_type == EventTypeEnum.user_create :
        db_session.add(Notification(notification.user_id, "user_create", notification_data=None, ))
        db_session.commit()
    elif notification.event_type == EventTypeEnum.change_password:
        print('password_changed')

init_db()

channel.basic_consume(
    queue=SETT.INSTANT_QUEUE, on_message_callback=callback, auto_ack=True)

channel.start_consuming()