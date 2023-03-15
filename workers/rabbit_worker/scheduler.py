import time

from mail_sender import send_mail
from schedule import every, repeat, run_pending
from sqlalchemy import or_

from config import settings as SETT
from db_conn import db_session
from db_models import Notification


@repeat(every().second)
def instant_notification_job():
    notifications = db_session.query(Notification).filter(or_(
                            Notification.notification_type=="user_create",
                            Notification.notification_type=="change_password"),
                            Notification.status==False)
    for n in notifications:
        try:
            send_mail(n.user_email, n.user_name, n.notification_text, template='instant')
            n.status = True
        except Exception as e:
            print(f"send_mail error - {e}") 
    db_session.commit()

while True:
    run_pending()
    time.sleep(1)
