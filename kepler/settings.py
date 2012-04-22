# Django settings for kepler project.
import os


DIRNAME = os.path.abspath(os.path.dirname(__file__))

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Admins', 'max@incuna.com'),
)

MANAGERS = ADMINS

EMAIL_SUBJECT_PREFIX = "[Kepler] "
SERVER_EMAIL = DEFAULT_FROM_EMAIL = "max@incuna.com"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'db.sqlite',                      # Or path to database file if using sqlite3.
        'USER': 'kepler',                      # Not used with sqlite3.
        'PASSWORD': '0y--DB_PASSWORD--)nr=9',                  # Not used with sqlite3.
        'HOST': '127.0.0.1',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/London'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-GB'

# Define the languages for the website
# See the docs: http://docs.djangoproject.com/en/dev/ref/settings/#languages
gettext = lambda s: s

LANGUAGES = (
    ('en', gettext('English')),
)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(DIRNAME, "client_media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/client_media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(DIRNAME, 'static_media')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = STATIC_URL +'admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    # ('', os.path.join(DIRNAME, "static")),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    #'compressor.finders.CompressorFinder',
)

## Registration settings

# No need to verify the account by email.
ACCOUNT_EMAIL_VERIFICATION = False

#LOGIN_URL = '/profile/login/'
#LOGOUT_URL = '/profile/logout/'
#LOGIN_REDIRECT_URL = '/'


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'KEY_PREFIX': 'kepler',
    }
}

# For dev
CACHES['default']['BACKEND'] = 'django.core.cache.backends.locmem.LocMemCache'


# Sorl settings
THUMBNAIL_SUBDIR = '_thumbs'
THUMBNAIL_QUALITY = 95


DATE_INPUT_FORMATS = ('%d/%m/%Y', '%d/%m/%y', '%Y-%m-%d', # '25/10/2006', '25/10/06', '2006-10-25'
                      '%b %d %Y', '%b %d, %Y',            # 'Oct 25 2006', 'Oct 25, 2006'
                      '%d %b %Y', '%d %b, %Y',            # '25 Oct 2006', '25 Oct, 2006'
                      '%B %d %Y', '%B %d, %Y',            # 'October 25 2006', 'October 25, 2006'
                      '%d %B %Y', '%d %B, %Y',            # '25 October 2006', '25 October, 2006'
                     )

DATE_FORMAT = 'd N Y'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'gqqb1r5hwtdcu@1^-+^ot2$zsdh_y-o1ljw6s9mq)qene%mt_a'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

# Cached template loader
# TEMPLATE_LOADERS = (
#     ('django.template.loaders.cached.Loader', (
#         'django.template.loaders.filesystem.Loader',
#         'django.template.loaders.app_directories.Loader',
#     )),
# )


from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    #  This context processor frequently causes transaction aborted errors!
)

MIDDLEWARE_CLASSES = (
    # 'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.doc.XViewMiddleware',
    #'pagination.middleware.PaginationMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',
)

ROOT_URLCONF = 'kepler.urls'

TEMPLATE_DIRS = (
    os.path.join(DIRNAME, "templates"),
)

SOUTH_MIGRATION_MODULES = {
    #'page': 'projectmigrations.page',
}

INSTALLED_APPS = (
    # project apps
    'kepler',
    'celestial',
    #'registration',
    #'pagination',
    #'crispy_forms',
    #'easy-thumbnails',
    #'compressor',
    'south',
    #'gunicorn',
    # django apps
    'django.contrib.humanize',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

#COMPRESS_CSS_FILTERS = [
#    'compressor.filters.css_default.CssAbsoluteFilter',
#    'compressor.filters.cssmin.CSSMinFilter',
#]

try:
    from local_settings import *
except ImportError:
    pass

