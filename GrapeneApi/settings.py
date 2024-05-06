from datetime import timedelta

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent




SECRET_KEY = 'django-insecure-mt%5rjlm4m2x^-uox%w80*_2pjx+7xcoe-j8u+&ms%0a9=b$ht'


DEBUG = True

ALLOWED_HOSTS = []


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10,
    'DATETIME_FORMAT': "%Y-%m-%dT%H:%M:%S%z",
    'DATE_FORMAT': "%Y-%m-%d",
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.AcceptHeaderVersioning'
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=15), #Токен истекает через 15 минут
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1), #Токен истекает через 1 день
    'ROTATE_REFRESH_TOKENS': True, #Отключаем ротацию токенов
    'BLACKLIST_AFTER_ROTATION': False, #Отключаем отключение токена после ротации
    'UPDATE_LAST_LOGIN': True, #Отключаем обновление даты последнего входа

    'ALGORITHM': 'HS256', #Алгоритм шифрования
    'SIGNING_KEY': SECRET_KEY, #Ключ шифрования
    'VERIFYING_KEY': None, #Ключ для проверки шифрования
    'AUDIENCE': None, #Аудитория

    'AUTH_HEADER_TYPES': ('Bearer',), #Типы заголовков для аутентификации
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM':'user_id',
}

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'rest_framework',
    'drf_yasg',
    'graphene_django',

    'main',
    'grapheneapi'



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

ROOT_URLCONF = 'GrapeneApi.urls'

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

WSGI_APPLICATION = 'GrapeneApi.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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


LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Asia/Almaty'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
