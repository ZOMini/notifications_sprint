import os
import smtplib
from email.message import EmailMessage

from jinja2 import Environment, FileSystemLoader

from workers.rabbit_worker.config import settings as SETT


def send_mail(to:str, name:str, data:str, template:str):
    server = smtplib.SMTP_SSL(SETT.SMTP_HOST, SETT.SMTP_PORT)
    server.login(user=SETT.SMTP_USER, password=SETT.SMTP_PASSWORD)
    message = EmailMessage()
    message["From"] = SETT.SMTP_USER
    message["To"] = to
    message["Subject"] = 'Уведомление :)'
    env = Environment(loader=FileSystemLoader(f'{os.path.dirname(__file__)}'))
    template = env.get_template(f'{template}.html')
    output = template.render(**{
        'title': f'Привет, {name}!',
        'text': f'{data}',
    })
    message.add_alternative(output, subtype='html')
    server.sendmail(from_addr=SETT.SMTP_USER, to_addrs=to, msg=message.as_string())
    server.close()
