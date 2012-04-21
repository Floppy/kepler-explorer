from settings import CACHES, DATABASES, INSTALLED_APPS, MIDDLEWARE_CLASSES

DEBUG = True
SERVE_MEDIA = DEBUG
TEMPLATE_DEBUG = DEBUG
EMAIL_DEBUG = DEBUG
THUMBNAIL_DEBUG = DEBUG

DEVELOPMENT_SITE = True

#COMPRESS_ENABLED = True
#DEBUG_PROPAGATE_EXCEPTIONS = False

DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'
DATABASES['default']['NAME'] = 'db.sqlite'
CACHES['default']['BACKEND'] = 'django.core.cache.backends.locmem.LocMemCache'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS = INSTALLED_APPS + (
    'debug_toolbar',
    'django_extensions',
)
MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + ('debug_toolbar.middleware.DebugToolbarMiddleware',)
INTERNAL_IPS = ('127.0.0.1',)

#DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False}
