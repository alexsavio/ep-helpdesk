"""
Django settings for ephelpdesk project.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

### General purpose Django settings

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("KEY") 

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG", "").lower() in ("true", "1")
# Force DEBUG to True, since the helpdesk doesn't run with DEBUG = False; see #2
#DEBUG = True

# Hosts allowed to contact us
ALLOWED_HOSTS = ['*']

# Site ID setting
SITE_ID = 1

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'markdown_deux',
    'bootstrapform', 	
    'helpdesk',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ephelpdesk.urls'

WSGI_APPLICATION = 'ephelpdesk.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'data/helpdesk.db'),
    }
}

# Templating engine
TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [
        os.path.join(BASE_DIR, 'helpdesk', 'templates'),
    ],
    'OPTIONS': {
        'debug': DEBUG,
        'context_processors': [
            "django.contrib.auth.context_processors.auth",
            'django.contrib.messages.context_processors.messages',
            "django.core.context_processors.i18n",
            "django.core.context_processors.debug",
            "django.core.context_processors.request",
            "django.core.context_processors.media",
            'django.core.context_processors.csrf',
            'django.core.context_processors.request',
            "django.core.context_processors.tz",
            "django.core.context_processors.static",
        ],
        'loaders': [
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        ],
    },
}]

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
MEDIA_URL = '/media/'
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
STATIC_ROOT = os.path.join(BASE_DIR, "static/")

# EMail settings
#EMAIL_HOST = os.environ.get("EMAIL_HOST") 
#EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER") 
#EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD") 
EMAIL_HOST = 'mail.europython.io'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''

### Helpdesk settings

# Show KB ?
HELPDESK_KB_ENABLED = True

# Allow changing password ?
# XXX There's a bug in the app which causes a:
#     NoReverseMatch at /dashboard/ - Reverse for 'auth_password_change' errors
#     when enabling this setting!
HELPDESK_SHOW_CHANGE_PASSWORD = False

# Helpdesk email subject
HELPDESK_EMAIL_SUBJECT_TEMPLATE = "{{ ticket.title|safe }} %(subject)s {{ ticket.ticket }}"

# Show tickets in public ?
HELPDESK_VIEW_A_TICKET_PUBLIC = False

# Allow public submission of tickets ?
HELPDESK_SUBMIT_A_TICKET_PUBLIC = False

# Hide assigned to in ticket submission form ?
HELPDESK_CREATE_TICKET_HIDE_ASSIGNED_TO = True

# Enable per-queue permissions to e.g. hide old queues ?
HELPDESK_ENABLE_PER_QUEUE_PERMISSION = True

# Login URL
LOGIN_URL = '/login/'
