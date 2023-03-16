import asyncio
import logging
import time

import aiohttp
import pika
from rabbit_models import NotificationEvent
from schedule import every, repeat, run_pending
from text_msg import MSG_TXT

from config import settings as SETT
from db_conn import db_session, init_db
from db_models import Notification, NotificationTypesEnum

init_db()

async def enrich_received_likes():
    notifications = db_session.query(Notification).filter(
        Notification.notification_type=="received_likes",
        Notification.status==False,
        Notification.ready==False
        )
    logging.error('ENRICH TICK')
    for n in notifications:
        logging.error('ENRICH NOTIF %s', n.user_id)
        try:
            async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=25, loop=asyncio.get_event_loop())) as client:
                async with client.get(f'{SETT.AUTH_URL}?id={n.user_id}') as resp:
                    if resp.status == 200:
                        logging.error('ENRICH - %s', resp.status)
                        _json = await resp.json()
                        print(_json)
                        n.user_email = _json['email']
                        n.user_name = _json['username']
                        n.ready = True
                        db_session.commit()
                    else:
                        logging.error('ENRICH FAIL - %s', resp.status)
                        db_session.rollback()
        except Exception as e:
            print(f"send_mail error - {e}") 

while True:
    asyncio.run(enrich_received_likes())
    time.sleep(5)
