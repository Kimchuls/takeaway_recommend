"""
Django settings for takeaway_pj project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zx457j%%1p^xv1qt7u(8!4r*%cz!ukoa*vsfse_o4d!hio5gg)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'login_module', # log in application module
    'index',
]

# SESSION_EXPIRE_AT_BROWSER_CLOSE=True
SESSION_COOKIE_AGE = 86400
SESSION_COOKIE_HTTPONLY = False
SESSION_COOKIE_SAMESITE=None

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 跨域
CORS_ALLOW_CREDENTIALS = True

CORS_ORIGIN_ALLOW_ALL=True

# CORS_ORIGIN_WHITELIST = (
#     # 'http://127.0.0.1:8000',
#     # 'http://localhost:8000',
#     'http://127.0.0.1:8080',
#     'http://0.0.0.0',
# )

CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
]

CORS_ALLOW_HEADERS = [
    'XMLHttpRequest',
    'X_FILENAME',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'Pragma',
]

ROOT_URLCONF = 'takeaway_pj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/index')],
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

WSGI_APPLICATION = 'takeaway_pj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 配置 MEDIA_ROOT 作为你上传文件在服务器中的基本路径
MEDIA_ROOT = os.path.join(BASE_DIR, 'upload') # 注意此处不要写成列表或元组的形式
# 配置 MEDIA_URL 作为公用 URL，指向上传文件的基本路径
MEDIA_URL = '/media/'
# 这里特意写成 upload 和 media，而不是统一写成 media 或 upload，是为了便于理解 MEDIA_ROOT 和 MEDIA_URL 的作用和区别


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    (os.path.join(BASE_DIR, 'static'))
]

EMAIL_USE_SSL = True
EMAIL_HOST = 'smtp.126.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'jincz2000@126.com'
EMAIL_HOST_PASSWORD = 'RUNSQTQECRPFHXPA'
DEFAULT_FROM_EMAIL = 'takeaway_recommend <jincz2000@126.com'