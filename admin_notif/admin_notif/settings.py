import logging
import os
from pathlib import Path

MONGO_HOST = os.environ.get('MONGO_NOTIF_HOST', '127.0.0.1')
MONGO_PORT = int(os.environ.get('MONGO_NOTIF_PORT', 27017))

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-d7#7wv1w*^8&zb_womidd597ui_z+3wa2hxb!6z(k8u5gx*10%'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'admin_notif.apps.AdminNotifConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'admin_notif.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'admin_notif.wsgi.application'

DATABASES = {
       'default': {
           'ENGINE': 'djongo',
           'NAME': 'notification',
           'CLIENT': {
                'host': MONGO_HOST,
                'port': MONGO_PORT,
            },
       }
   }

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EXT_LOGGING = os.environ.get('EXT_LOGGING', False)
if not EXT_LOGGING:
    logging.error(EXT_LOGGING)
    LOGGER_HOST = os.environ.get('LOGSTASH_HOST', 'logstash')
    LOGGER_PORT = int(os.environ.get('LOGSTASH_PORT', 5044))
    LOG_LEVEL = 'INFO'
    LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
                'format': 'velname)s %(message)s'
            },
    },
    'handlers': {
            'console': {
                'level': LOG_LEVEL,
                'class': 'logging.StreamHandler',
                'formatter': 'simple'
            },
            'logstash': {
                'level': LOG_LEVEL,
                'class': 'logstash.LogstashHandler',
                'host': LOGGER_HOST,
                'port': LOGGER_PORT, 
                'version': 1,
                'message_type': 'django',
                'fqdn': False,
                'tags': ['django'],
            },
    },
    'loggers': {
            'django.request': {
                'handlers': ['logstash'],
                'level': LOG_LEVEL,
                'propagate': True,
            },
        },
    }
