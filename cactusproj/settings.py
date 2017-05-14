import os

BASE_DIR = os.path.dirname(__file__)

SECRET_KEY = 'dev_secret_key'
DEBUG = True
SOCIAL_PROD = False

ALLOWED_HOSTS = ['localhost', '10.55.28.66', '192.168.99.100']

# Application definition
INSTALLED_APPS = [
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.humanize',
    # third party apps
    'social_django',
    'crispy_forms',
    'imagekit',
    'widget_tweaks',
    'django_countries',
    'django_extensions',
    'rest_framework',
    # custom apps
    'cactusproj.accounts',
    'cactusproj.landing',
    'cactusproj.utils',
    'cactusproj.chat',
    'cactusproj.core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'cactusproj.urls'

SITE_ID = 1

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
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

WSGI_APPLICATION = 'cactusproj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/webapps/www/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Cache
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://redis:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

# Media
MEDIA_URL = '/media/'
MEDIA_ROOT = '/webapps/www/media/'

# Grapelli Admin Theme
GRAPPELLI_ADMIN_TITLE = 'City Lights'

# Fork of Registration Redux
INCLUDE_REGISTER_URL = False    # for basic stuff
DISABLE_REGISTRATION = False   # for other stuff from registration, for example token management
LOGIN_REDIRECT_URL = "landing:main_page"


# CELERY SETTINGS
CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'


# Crispy Forms
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# Rest Framework
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}


# Social Part
AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.vk.VKOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

if SOCIAL_PROD:
    # Social Auth (prod)
    SOCIAL_AUTH_VK_OAUTH2_KEY = '5925244'
    SOCIAL_AUTH_VK_OAUTH2_SECRET = '1WVpRCpclGsYtCn4ZRPo'
    SOCIAL_AUTH_FACEBOOK_KEY = '414207582263848'  # App ID
    SOCIAL_AUTH_FACEBOOK_SECRET = 'a9c16819586592d45d12566a39fd7d4f'  # App Secret
else:
    # Social Auth (dev)
    SOCIAL_AUTH_VK_OAUTH2_KEY = '5924892'
    SOCIAL_AUTH_VK_OAUTH2_SECRET = 'w3c5l7PF2JhsCtwFypAI'
    SOCIAL_AUTH_FACEBOOK_KEY = '1867867903482887'  # App ID
    SOCIAL_AUTH_FACEBOOK_SECRET = '200074daf90465f73569843d4232b4bc'  # App Secret


SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)


LOGIN_URL = 'accounts:login'
LOGOUT_URL = 'accounts:logout'
LOGOUT_REDIRECT_URL = 'accounts:login'
LOGIN_REDIRECT_URL = 'landing:main_page'
SOCIAL_AUTH_LOGIN_ERROR_URL = 'accounts:login'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = 'accounts:redirect'
SOCIAL_AUTH_RAISE_EXCEPTIONS = False
