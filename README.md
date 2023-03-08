# Проектная работа 10 спринта

Проектные работы в этом модуле в команде. Задания на спринт вы найдёте внутри тем.

# Сделано
  - на 08.03
  - Админка(Django)
  - API(FastApi)  
  - Все хранится в mongo(решил попробывать mongo c django. Гемор, но вроде работает - движок djOngo)
  - доделываю api, под него воркеры, в конце рабита прикручу.
  - Прикручиваю flask_auth и movies_fastapi, от них ивенты будут.

# Полезности
  - docker-compose -f docker-compose-notif.yml up --build
  - docker-compose -f docker-compose-ugc.yml -f docker-compose-log.yml up --build 
  - docker-compose -f docker-compose-log.yml -f docker-compose-all_prev_serv.yml up --build
  - для разработки auth+logs+notif:
    - docker-compose -f docker-compose-notif.yml -f docker-compose-all_prev_serv.yml -f docker-compose-log.yml up --build
  - для разработки все сервисы(16gb+ RAM):
    - docker-compose -f docker-compose-notif.yml -f docker-compose-all_prev_serv.yml -f docker-compose-log.yml -f docker-compose-ugc.yml up --build