"""
Django settings for oct_victory project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'r%jw7w@_7nqj&v^r6k3l0f^^60wqmyumo=)r3w!^&f$ofa9#88'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django_extensions',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'board',
    'accounts',
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

ROOT_URLCONF = 'oct_victory.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # render(request, 'HERE')  HERE 파일을 찾을 때, 어떤 폴더를 들여다 볼 것인가..?
            # 기본적으로 Default로 INSTALLED_APPS 에 등록된 APP/templates/ 안을 찾아봅니다.
            # 추가적으로 여기(PROJECT/templates)도 찾아주세요..
            os.path.join(BASE_DIR, 'templates')
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

WSGI_APPLICATION = 'oct_victory.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ko-kr'
# 저장되는 DateTimeField 의 값이 바뀌는게 아니라 표시되는 시간이 바뀜
TIME_ZONE = 'Asia/Seoul'  # UTC  <=  CUT(Coordinated Universal Time)  TUC(Temps Universel Coordonnel)
# 국제화 대응 I nternationalization N
USE_I18N = True
# 현지화 대응 L ocalizatio N
USE_L10N = True
# 이걸 False 로 바꾸면, 저장도 Asia/Seoul
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

# static files == 서버가 쓰려고 준비한 파일(CSS, JS, Images) - 빌트인 옵션

# 우리 서버에서 static 파일을 제공할 때, 필요한 URL 접두사.
STATIC_URL = '/static/'

# 우리가 static files 를 둘 곳
STATICFILES_DIRS = [
    # {% static 'HERE' %}  HERE 파일을 찾을 때, 어떤 폴더를 들여다 볼 것인가..?
    # 기본적으로 Default로 INSTALLED_APPS 에 등록된 APP/static/ 안을 찾아봅니다.
    # 추가적으로 여기(PROJECT/assets/)도 찾아주세요..
    os.path.join(BASE_DIR, 'assets'),
]

# media files == 클라이언트가 업로드하는 파일(*.*) - 사용자 맘대로 올리는 것
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')