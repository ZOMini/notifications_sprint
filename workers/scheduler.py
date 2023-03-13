from schedule import repeat, run_pending, every
import time
from db_models import Notification
from db import db_session
from mail_sender import send_mail


@repeat(every().second)
def instant_notification_job():
    notifications = db_session.query(Notification).filter(
                            Notification.notification_type=="user_create",
                            Notification.status==False)
    for n in notifications:
        try:
            send_mail("ingvarsinn@yandex.ru", n.user_id, Notification.notification_data, template='instant')
            n.status = True
        except Exception as e:
            print("error")
    db_session.commit()

while True:
    run_pending()
    time.sleep(1)