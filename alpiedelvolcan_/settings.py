"""
Django settings for alpiedelvolcan_ project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-71ilsry+%0yrbexaf^j!f41b0i=t!g+8%pvd!1d8a)azph_nd-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['alpiedelvolcan.azurewebsites.net', 'http://0.0.0.0:8000/', '127.0.0.1', 'volcanosm.net']
#CORS_ALLOWED_ORIGINS = ['https://alpiedelvolcan.azurewebsites.net/']

# Security & HTTPS settings
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = False

CORS_ALLOW_ALL_ORIGINS = True
CSRF_TRUSTED_ORIGINS = ['https://alpiedelvolcan.azurewebsites.net', 'https://volcanosm.net']




EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mail.ceinversiones.com'
EMAIL_PORT = 465
EMAIL_USE_SSL = True
EMAIL_HOST_USER = 'fvillalta@ceinversiones.com'
EMAIL_HOST_PASSWORD = 'YrN.yYX-8uuz'
# DEFAULT_FROM_EMAIL = 'fvillalta@alpiedelvolcan.com'
# EMAIL_BACKEND = 'sendgrid_backend.SendgridBackend'
# SENDGRID_API_KEY = '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'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'Tours',
    'Servicios',
    'Configuraciones',
    'Nosotros',
    'Contactanos',
    'Transacciones',
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

ROOT_URLCONF = 'alpiedelvolcan_.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'templates/sections'),
            os.path.join(BASE_DIR, 'Tours/templates'),
            os.path.join(BASE_DIR, 'Servicios/templates'),
            os.path.join(BASE_DIR, 'Nosotros/templates'),
            os.path.join(BASE_DIR, 'Contactanos/templates'),
            os.path.join(BASE_DIR, 'Configuraciones/templates'),
            os.path.join(BASE_DIR, 'Transacciones/templates'),
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

WSGI_APPLICATION = 'alpiedelvolcan_.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'sqlite': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cuadmesv_tour',
        'USER': 'cuadmesv_tour',
        'PASSWORD': '8LC*do.&7Emh',
        'HOST': 'www.metrocuadrado.com.sv',
        'PORT': '3306',  # Puerto predeterminado de MySQL
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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

# Configuración regional para El Salvador
LANGUAGE_CODE = 'es-SV'
TIME_ZONE = 'America/El_Salvador'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# Configuración para archivos estáticos
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = '/static/'



# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')