[![Notification workflows](https://github.com/ZOMini/notifications_sprint_1/actions/workflows/python.yml/badge.svg)](https://github.com/ZOMini/notifications_sprint_1/actions/workflows/python.yml)

# Нотификация

## Описание
  - Сервис нотификации отправляет сообщения пользователю на определенные события (поступающие от сервисов авторизации и UGC).
  - Сервис объединен с ранее написанными сервисами [AUTH](https://github.com/ZOMini/Auth_sprint_2) и [UGC](https://github.com/ZOMini/ugc_sprint_2)
  - UGC(kafka, click house) отключил, так как notif + auth + kafka и click house(4-е нода) слишком много для одного docker-compose, нужно разносить на разные сервера.

## Стек
  - RabbitMQ, Kafka, Click House, FastAPI, MongoDB, Mailhog, Flask, SQLAlchemy, Flask, aiohttp, Django

## Работа
  - docker-compose -f docker-compose-notif_new.yml up --build    все работает сходу
  - http://127.0.0.1:5000/auth/docs/v1  ~ тут можно создать пользователя/сменить пароль - полетит ивент
  - http://127.0.0.1:8000/ugc/api/openapi ~ тут можно создать ревью(нужен реальный id юзера, см. выше) и лайкнуть его - полетит ивент
  - http://127.0.0.1:8082/notif/admin ~ тут можно создать рассылку по списку id пользователей и вообще посмотреть все ивенты.
  - http://127.0.0.1:15672/ ~ rabbit gui (admin/123456789)
  - http://127.0.0.1:8025/ ~ mailhog gui

## Сделано
  - на 08.03
    - Админка(Django)
    - API(FastApi)  
    - Все хранится в mongo(решил попробывать mongo c django. Гемор, но вроде работает - движок djOngo)
    - доделываю api, под него воркеры.
    - Прикручиваю flask_auth и movies_fastapi, от них ивенты будут.
  - на 15.03(Все полностью переделали!)
    - http://127.0.0.1:8000/ugc/api/openapi   - ugc docs
    - http://127.0.0.1:5000/auth/docs/v1     - auth docs
    - http://127.0.0.1:15672/    - rabbit gui (admin/123456789)
    - все сервисы можно запускать локально (docker-compose -f docker-compose-notif_new.yml up --build) , дропаем сервис - запускаем локально:
    - flask_auth/python app.py
    - ugc_api/python main.py
    - workers/python rabbit_worker.py
    - workers/python enrichment_worker.py
    - workers/python sender_worker.py
    - делаю еще 2-а вокера, обогатителя данными и емаил сендера
  - еще 16.03
    - добавил воркера который обогощает данными ивенты от ugc
    - добавил воркера сендера
    - остался админ вариант
  - 17.03
    - добавил админ панель, для создания списка пользователей и текста сообщения, по нему enrich_worker формирует данные для сендера.
    - плюс архитектура

## Полезности
  - docker-compose -f docker-compose-notif_new.yml up --build
  - смотрим notif_db в шеле контейнера:
    - psql -U app -h localhost -d notif_db
    - SELECT * FROM notifications;
    - SELECT * FROM adminnotifevent;
  - смотрим auth_db в шеле контейнера:
    - psql -U app -h localhost -d auth_db
    - SELECT * FROM users;
  - SELECT * FROM pg_catalog.pg_tables;

## Для проверки:
  - https://github.com/ZOMini/notifications_sprint_1  - репозиторий
  - https://github.com/ZOMini/notifications_sprint_1/invitations - приглашение
  - группа 6 - Пирогов Виталий/Игорь Синякин(@ee2 @sinyakinmail - в пачке) 