"""
Django settings for ems_core project.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ------------------------
# BASE DIRECTORY
# ------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# ------------------------
# SECURITY SETTINGS
# ------------------------
SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-default-key")
DEBUG = os.getenv("DEBUG", "True") == "True"
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")

# ------------------------
# APPLICATIONS
# ------------------------
INSTALLED_APPS = [
    # Django Core
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third Party
    'rest_framework',
    'corsheaders',

    # Local Apps
    #'users',
    #'employees',
    #'attendance',
    #'payroll',
    #'reports',
]

# ------------------------
# MIDDLEWARE
# ------------------------
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # must come before CommonMiddleware
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ------------------------
# URLS / WSGI
# ------------------------
ROOT_URLCONF = 'ems_core.urls'
WSGI_APPLICATION = 'ems_core.wsgi.application'

# ------------------------
# TEMPLATES
# ------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # global templates folder
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

# ------------------------
# DATABASE
# ------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # can change to PostgreSQL later
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ------------------------
# PASSWORD VALIDATORS
# ------------------------
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

# ------------------------
# INTERNATIONALIZATION
# ------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Dhaka'
USE_I18N = True
USE_TZ = True

# ------------------------
# STATIC & MEDIA
# ------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

# ------------------------
# DEFAULT PRIMARY KEY FIELD TYPE
# ------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ------------------------
# CUSTOM USER MODEL
# ------------------------
#AUTH_USER_MODEL = "users.User"

# ------------------------
# EMAIL CONFIG
# ------------------------
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
DEFAULT_FROM_EMAIL = "noreply@ems.com"

# ------------------------
# CORS SETTINGS
# ------------------------
CORS_ALLOW_ALL_ORIGINS = True

# ------------------------
# REST FRAMEWORK CONFIG
# ------------------------
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

# ------------------------
# JWT SETTINGS (optional customization)
# ------------------------
from datetime import timedelta
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'AUTH_HEADER_TYPES': ('Bearer',),
}


