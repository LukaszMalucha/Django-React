

import os
import environ
from pathlib import Path
from datetime import timedelta


BASE_DIR = Path(__file__).resolve().parent.parent



env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env()

if "SECRET_KEY" in os.environ:
    SECRET_KEY = env("SECRET_KEY")
    DEBUG = env("DEBUG")
    DB_NAME = env("DB_NAME")
    DB_USER = env("DB_USER")
    DB_PASSWORD = env("DB_PASSWORD")
    DB_HOST = env("DB_HOST")

else:
    SECRET_KEY = "testing_ci"
    DEBUG = True
    DB_NAME = "test"
    DB_USER = "test"
    DB_PASSWORD = "test"
    DB_HOST = "test"

ALLOWED_HOSTS = ["*"]



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',

    # BRUTE FORCE COUNTER
    "axes",

    "corsheaders",
    "storages",

    "rest_framework",
    "rest_framework.authtoken",

    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "dj_rest_auth.registration",

    'webpack_loader',

    "api",
    "core",
    "db_manager",
    "user",

    "xrp_ledger"

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    # AUTO-LOGOUT
    "django_auto_logout.middleware.auto_logout",

    # Brute Force counter
    "axes.middleware.AxesMiddleware",
]

ROOT_URLCONF = 'portal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        "DIRS": [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'portal.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# AUTHENTICATION
AUTHENTICATION_BACKENDS = [
    "axes.backends.AxesStandaloneBackend",
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

# AUTO LOGOUT
AUTO_LOGOUT = {
    'IDLE_TIME': timedelta(minutes=30),
    'REDIRECT_TO_LOGIN_IMMEDIATELY': True,
}

SITE_ID = 1

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_LOGIN_METHODS = {'email'}
ACCOUNT_UNIQUE_EMAIL = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


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

# LOCALIZATION
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True



STATIC_URL = 'static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)




WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'webpack_bundles/',
        'CACHE': not DEBUG,
        "STATS_FILE": os.path.join(BASE_DIR, "frontend", "webpack-stats.json"),
        'POLL_INTERVAL': 0.1,
        'IGNORE': [r'.+\.hot-update.js', r'.+\.map'],
    }
}

# AWS SES
EMAIL_BACKEND = "django_ses.SESBackend"
AWS_SES_REGION_NAME = "eu-west-1"
AWS_SES_REGION_ENDPOINT = "email.eu-west-1.amazonaws.com"


# COUNTER BRUTEFORCE
AXES_FAILURE_LIMIT: 3 # Failures count
AXES_COOLOFF_TIME: 0.01 # hours
AXES_REST_ON_SUCCESS = True # Reset failed login attempts. To reset: python manage.py axes_reset
AXES_LOCKOUT_TEMPLATE = "account-locked.html"


# DEPLOYMENT
if not DEBUG:

    SESSION_COOKIE_SECURE = True
    CSRF_COOKIES_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_SECONDS = 315336000
    SECURE_HSTS_PRELOAD = True
    SECURE_HSTS_INCLUDE_SUBDOMAIN = True
    SECURE_REDIRECT_EXEMPT = []
    SECURE_SSL_REDIRECT = True



    # DATABASES = {
    #     "default": {
    #         "ENGINE": "django.db.backends.postgresql",
    #         "NAME": DB_NAME,
    #         "USER": DB_USER,
    #         "PASSWORD": DB_PASSWORD,
    #         "HOST": DB_HOST,
    #         "PORT": 5432,
    #     },
    # }

    #     # s3 static settings

    STATIC_LOCATION = "static"
    PUBLIC_MEDIA_LOCATION = "media"
    MEDIA_LOCATION = "media"

    AWS_DEFAULT_ACL = None
    AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME")
    AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
    AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}
    STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/"
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

    # MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/"

