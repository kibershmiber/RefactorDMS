import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# session
SESSION_ENGINE = 'django.contrib.sessions.backends.file'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

ROOT_URLCONF = 'system.urls'

WSGI_APPLICATION = 'system.wsgi.application'

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
)

TIME_ZONE = 'Europe/Kiev'
LANGUAGE_CODE = 'uk_UA'
DEFAULT_CHARSET = 'utf8'

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join('static'),)

CONN_MAX_AGE = None
