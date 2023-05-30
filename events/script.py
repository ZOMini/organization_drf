import os
import runpy
import sys
import time

from dotenv import load_dotenv

from events.wsgi import *

load_dotenv()

time.sleep(1)  # Ждем на всякий.

# Миграции Django.
sys.argv = ['', 'makemigrations', 'api']
runpy.run_path('./manage.py', run_name='__main__')

sys.argv = ['', 'migrate']
runpy.run_path('./manage.py', run_name='__main__')

# Собираем статику.
sys.argv = ['', 'collectstatic', '--noinput']
runpy.run_path('./manage.py', run_name='__main__')

# Создаем организацию.
from api.models import Organization

org = Organization.objects.get_or_create(
    title='AdminGroup',
    description='For staff',
    address='address',
    postcode='699999',)

# Создаем суперпользователя.
email = os.environ.get('ADMIN_EMAIL', 'admin@example.com')
password = os.environ.get('SUPERPASS', 'qwer1234')
sys.argv = ['', 'create_superuser2', '--email', email, '--password', password, '--organization', str(org[0].id), '--noinput', '--preserve']
runpy.run_path('./manage.py', run_name='__main__')

