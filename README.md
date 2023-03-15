# Проектная работа 10 спринта

Проектные работы в этом модуле в команде. Задания на спринт вы найдёте внутри тем.

# Сделано
  - на 08.03
    - Админка(Django)
    - API(FastApi)  
    - Все хранится в mongo(решил попробывать mongo c django. Гемор, но вроде работает - движок djOngo)
    - доделываю api, под него воркеры, в конце рабита прикручу.
    - Прикручиваю flask_auth и movies_fastapi, от них ивенты будут.
  - на 15.03(Все полностью переделали!)
    - http://127.0.0.1:8000/ugc/api/openapi   - ugc docs
    - http://127.0.0.1:5000/auth/docs/v1     - auth docs
    - http://127.0.0.1:15672/    - rabbit gui (admin/123456789)
    - все сервисы можно запускать локально (docker-compose -f docker-compose-notif_new.yml up --build) , дропаем сервис - запускаем локально:
    - flask_auth/python app.py
    - ugc_api/python main.py
    - workers/rabbit_worker/python main.py
    - делаю еще 2-а вокера, обогатителя данными и емаил сендера
# Полезности
  - docker-compose -f docker-compose-notif_new.yml up --build
  - смотрим notif_db в шеле контейнера:
    - psql -U app -h localhost -d notif_db
    - SELECT * FROM notifications;
  - смотрим auth_db в шеле контейнера:
    - psql -U app -h localhost -d auth_db
    - SELECT * FROM users;