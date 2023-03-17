import runpy
import sys
import time

time.sleep(5)

# Миграции Django.
sys.argv = ['', 'makemigrations']
runpy.run_path('./manage.py', run_name='__main__')

# Миграции Django.
sys.argv = ['', 'migrate', 'admin_notif', '--fake']
runpy.run_path('./manage.py', run_name='__main__')

# Миграции Django.
sys.argv = ['', 'migrate']
runpy.run_path('./manage.py', run_name='__main__')

# Собираем статику.
sys.argv = ['', 'collectstatic', '--noinput']
runpy.run_path('./manage.py', run_name='__main__')

# Создаем суперпользователя(superuser/password).
runpy.run_path('./scripts/create_superuser.py', run_name='__main__')
