import runpy
import sys

# Миграции Django.
sys.argv = ['', 'migrate']
runpy.run_path('./manage.py', run_name='__main__')

# Собираем статику.
sys.argv = ['', 'collectstatic', '--noinput']
runpy.run_path('./manage.py', run_name='__main__')

# Создаем суперпользователя(superuser/password).
runpy.run_path('./scripts/create_superuser.py', run_name='__main__')
