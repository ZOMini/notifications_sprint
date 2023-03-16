import logging
import time

from mail_sender import send_mail
from schedule import every, repeat, run_pending
from sqlalchemy import or_

from config import settings as SETT
from db_conn import db_session
from db_models import Notification


@repeat(every().second)
def instant_notification_job():
    print('instant_notification_job()')
    notifications = db_session.query(Notification).filter(or_(
            Notification.notification_type=="user_create",
            Notification.notification_type=="change_password"),
            Notification.ready==True,
            Notification.status==False)
    for n in notifications:
        try:
            # send_mail(n.user_email, n.user_name, n.notification_text, template='instant')
            logging.error(n.user_email, n.user_name, n.notification_text, 'inst send mail')
            n.status = True
            db_session.commit()
        except Exception as e:
            db_session.rollback()

# @repeat(every().day.at('10:30'))
@repeat(every(20).seconds)
def deferred_notification_job():
    user_ids = db_session.query(Notification.user_id).filter(
            Notification.notification_type=="received_likes",
            Notification.ready==True,
            Notification.status==False).distinct()
    for id in user_ids:
        try:
            notif_user = db_session.query(Notification).filter(
                Notification.user_id==id[0],
                Notification.ready==True,
                Notification.status==False).all()
            for n in notif_user:
                n.status = True
            cnt = len(notif_user)
            # send_mail(n.user_email, 
            #           n.user_name,
            #           f'На ваши ревью поставили {cnt} лайков! Ждем в гости!',
            #           template='instant')
            logging.error(n.user_email, n.user_name, cnt, 'лайков! Ждем в гости!')
            db_session.commit()
        except:
            db_session.rollback()
    

while True:
    run_pending()
    time.sleep(1)
