"""
Django settings for NewsPortal project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

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
    # my app
    'Accounts',
    'Portal',
    # other app
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.yandex',
    'django_filters'
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

ROOT_URLCONF = 'NewsPortal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # Для работы allauth
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'NewsPortal.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Настройки дописаные мною
# Нужна для корректности работы некоторых приложений
SITE_ID = 1
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]
# Куда перенаправлять после входи или выхода
LOGIN_REDIRECT_URL = '/news/'
LOGOUT_REDIRECT_URL = '/news/'

# Добавляем константу для папки статик где лежит ксс у нас
STATICFILES_DIRS = [BASE_DIR / "static"]

# Настройки allauth
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = 'none'
# Добавляем свою форму регистрации
ACCOUNT_FORMS = {
    'signup': 'Accounts.forms.CastomCreateUser',
}

# Настраиваем логирование
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'filters': {
        'debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },


    'handlers': {
        'console_debug': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'debug',
            'filters': ['debug_true'],
        },
        'console_warning': {
            'level': 'WARNING',
            'class': 'logging.StreamHandler',
            'formatter': 'warning',
            'filters': ['debug_true'],
        },
        'console_error': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'error and critical',
            'filters': ['debug_true'],
        },
        'general_info': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': f'{BASE_DIR}/log/general.log',
            'formatter': 'general_security',
            'filters': ['debug_false'],
        },
        'errors': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': f'{BASE_DIR}/log/errors.log',
            'formatter': 'error and critical',
        },
        'security': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': f'{BASE_DIR}/log/security.log',
            'formatter': 'general_security',
        },
        'mail_error': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'warning',
            'filters': ['debug_false'],
        },
    },

    'loggers': {
        'django': {
            'handlers': ['console_debug', 'console_warning',
                         'console_error', 'general_info'],
            'level': 'DEBUG',
        },
        'django.request': {
            'handlers': ['errors', 'mail_error'],
            'level': 'ERROR',
        },
        'django.server': {
            'handlers': ['errors', 'mail_error'],
            'level': 'ERROR',
        },
        'django.template': {
            'handlers': ['errors'],
            'level': 'ERROR',
        },
        'django.db.backends': {
            'handlers': ['errors'],
            'level': 'ERROR',
        },
        'django.security': {
            'handlers': ['security'],
            'level': 'DEBUG',
        },
    },

    'formatters': {
        'debug': {
            'format': '({asctime}) {levelname} {message}',
            'style': '{',
        },
        'warning': {
            'format': '({asctime}) {levelname} {pathname}'
                      '{message}',
            'style': '{',
        },
        'error and critical': {
            'format': '({asctime}) {levelname} {pathname}'
                      '{exc_info} {message}',
            'style': '{',
        },
        'general_security': {
            'format': '({asctime}) {levelname} {module} '
                      '{message}',
            'style': '{',
        },
    },
}
