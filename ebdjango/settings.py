"""
Django settings for ebdjango project.

Generated by 'django-admin startproject' using Django 1.9.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
##secret test key from api stripe site 
SECRET_KEY = 'sk_test_3CGVcNJRchvGx7zp17jBIgRD'
##PUBLISHABLE KEY from strip:'pk_test_liZCnyfYKT14az1lNtQHGB2k'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1','http://291d762f.ngrok.io']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'main',
    'account',
    'django_forms_bootstrap',
    #'debug_toolbar',
    'tinymce',
    'emoticons',
    'django.contrib.sites',
    'disqus',
    'paypal.standard.ipn',
    'paypal_store',
    'products',
    'magazines',
    'threads',
    'polls',
    #'django-gravatar',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django_forms_bootstrap',
    'paypal.standard.ipn',
    'rest_framework',
    'tinymce',
    'emoticons',
    'disqus',
    'reusable_blog',
    'home',
    'accounts',
    'paypal_store',
    'products',
    'magazines',
    'threads',
    'polls',
]
DISQUS_WEBSITE_SHORTNAME = 'tastytimesblog'
SITE_ID = 1

INTERNAL_IPS = ('127.0.0.1',)

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]
ROOT_URLCONF = 'ebdjango.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'ebdjango.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

if 'RDS_HOSTNAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
#    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "media/images"),
)
#STATIC_ROOT = 'static'
TEMPLATE_DIRS = (
'ebdjango/ebdjango/templates',
'ebdjango/templates',
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

#Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', ' pk_test_liZCnyfYKT14az1lNtQHGB2k ')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', ' sk_test_3CGVcNJRchvGx7zp17jBIgRD ')


# Account: to tell Django we want to use this class as our User class
AUTH_USER_MODEL = 'account.User'
 
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'account.backends.EmailAuth',
)

#Stripe
SITE_ID = 1
STRIPE_PUBLISHABLE = "pk_test_liZCnyfYKT14az1lNtQHGB2k"
STRIPE_SECRET = "sk_test_3CGVcNJRchvGx7zp17jBIgRD"

#TinyMCE settings
TINYMCE_JS_ROOT = os.path.join(BASE_DIR, "static", "js",
                               "tinymce", "tinymce.min.js")

# PayPal Settings
SITE_URL = 'http://tastytimes.herokuapp.com/'
PAYPAL_NOTIFY_URL = 'http://tastytimes.herokuapp.com/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = 'alinechribeiro-facilitator@gmail.com'