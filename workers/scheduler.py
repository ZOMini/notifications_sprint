from schedule import repeat, run_pending, every
import time
from db_models import Notification
from db import db_session
from mail_sender import send_mail
from config import settings as SETT
from db_models import User

@repeat(every().second)
def instant_notification_job():
    notifications = db_session.query(Notification).join(User).filter(
                            Notification.notification_type=="user_create",
                            Notification.status==False)
    for n in notifications:
        try:
            send_mail(n.user.email, n.user.name, "Вы успешно зарегистрировались!", template='instant')
            n.status = True
        except Exception as e:
            print("error")
    db_session.commit()

while True:
    run_pending()
    time.sleep(1)