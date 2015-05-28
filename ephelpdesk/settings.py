"""
Django settings for ephelpdesk project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("KEY") 

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG", "").lower() in ("true", "1")

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

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
    #'django.contrib.markup', #DEPRECATED
    'django.contrib.humanize',
    #'south',
    'markdown_deux',
    'helpdesk',
    'bootstrapform', 	
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
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'data/helpdesk.db'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
STATIC_ROOT = os.path.join(BASE_DIR, "static/")

#EMAIL_HOST = os.environ.get("EMAIL_HOST") 
#EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER") 
#EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD") 
EMAIL_HOST = 'mail.europython.io'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''

### Helpdesk settings

# Show KB ?
HELPDESK_KB_ENABLED = False

# Allow changing password ?
# XXX There's a but in the app which causes a:
#     NoReverseMatch at /dashboard/ - Reverse for 'auth_password_change' errors
#     when enabling this setting!
HELPDESK_SHOW_CHANGE_PASSWORD = False

# Helpdesk email subject
HELPDESK_EMAIL_SUBJECT_TEMPLATE = "{{ ticket.title|safe }} %(subject)s {{ ticket.ticket }}"

# Show tickets in public ?
HELPDESK_VIEW_A_TICKET_PUBLIC = False

# Hide assigned to in ticket submission form ?
HELPDESK_CREATE_TICKET_HIDE_ASSIGNED_TO = True

