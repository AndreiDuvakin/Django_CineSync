import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', default='google')

DEBUG = os.getenv('DJANGO_DEBUG', default='false')
DEBUG = DEBUG.lower().strip() in ('true', 'yes', '1', 'y', 't')

AUTH_USER_MODEL = 'auth.User'

ALLOWED_HOSTS = os.getenv(
    'DJANGO_ALLOWED_HOSTS',
    default=[
        'localhost,127.0.0.1',
    ],
).split(',')

INSTALLED_APPS = [
    'films.apps.FilmsConfig',
    'home.apps.HomeConfig',
    'tickets.apps.TicketsConfig',
    'timetable.apps.TimetableConfig',
    'users.apps.UsersConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sorl.thumbnail',
    'ckeditor',
    'django_cleanup.apps.CleanupConfig',
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

if DEBUG:
    INSTALLED_APPS += [
        'debug_toolbar',
    ]
    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]

ROOT_URLCONF = 'CineSync.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
        ],
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

INTERNAL_IPS = [
    '127.0.0.1',
    'localhost',
]

WSGI_APPLICATION = 'CineSync.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DJANGO_DB_NAME', default='cinesync_db'),
        'USER': os.getenv('DJANGO_DB_USER', default='cinesync'),
        'PASSWORD': os.getenv('DJANGO_DB_PASSWORD'),
        'HOST': os.getenv('DJANGO_DB_HOST', default='localhost'),
        'PORT': os.getenv('DJANGO_DB_PORT', default='5432'),
    },
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.'
                'password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.'
                'password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.'
                'password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.'
                'password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'

LOGIN_URL = '/auth/login/'

LOGIN_REDIRECT_URL = '/'

LOGOUT_REDIRECT_URL = '/auth/login/'
