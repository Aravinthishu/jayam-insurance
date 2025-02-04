"""
Django settings for jayaminsurance project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import os
from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['jayaminsurance.com', '*', 'www.jayaminsurance.com']


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'sitesettings',
    'index',
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

ROOT_URLCONF = 'jayaminsurance.urls'

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
                
                'sitesettings.context_processors.site_settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'jayaminsurance.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',  # MySQL database engine
#         'NAME': 'jayam',          # Your MySQL database name
#         'USER': 'Admin',             # Your MySQL username
#         'PASSWORD': 'Webteam@Ec4you',     # Your MySQL password
#         'HOST': 'localhost',                   # Database host, use 'localhost' or an IP address
#         'PORT': '3306',                        # Default MySQL port
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]  # Global static folder
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Directory for collected static files (for deployment)


MEDIA_URL = '/media/'  # URL to access media files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')  # Path to store media files

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Email configuration

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER=config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD=config('EMAIL_HOST_PASSWORD')
EMAIL_HOST_USER_NAME=config('EMAIL_HOST_USER_NAME')
ADMIN_EMAIL=config('ADMIN_EMAIL')
ADMIN_EMAIL2=config('ADMIN_EMAIL2')

#Jazzmin Settings

JAZZMIN_SETTINGS = {
    "site_title": "Jayam Insurance",  # Title of the admin site
    "site_header": "My Admin",  # Header displayed on the admin site
    "site_brand": "Jayam Insurance and Management",  # Brand name displayed in the admin
    "welcome_sign": "Welcome to the Admin Panel!",  # Welcome message
    "show_ui_builder": True,  # Show UI builder for customization
    "changeform_format": "horizontal",  # Form layout (options: 'vertical', 'horizontal')
    "use_google_fonts": True,  # Whether to use Google Fonts
    # Add more options here based on your requirements
    
    "icons": {
        "auth.User": "fas fa-user",
        "auth.Group": "fas fa-users",
        "sitesettings.Brand": "fas fa-cogs",  # Custom icon for MyModel in your app
        "sitesettings.Social_links": "fas fa-link",
        "index.HeroSection": "fas fa-home",
        "index.AboutSection": "fas fa-info",
        "index.InsuranceSection": "fas fa-shield-alt",
        "index.Testimonial": "fas fa-comments",
        "index.Contact": "fas fa-phone",
        "index.PartnerLogo": "fas fa-users",
        "index.ClientLogo": "fas fa-users",
        "index.Certificate": "fa fa-certificate",
        "sitesettings.Address": "fa fa-directions",
        "sitesettings.updates": "fas fa-sync",
    },
}


JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-primary",
    "navbar": "navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "darkly",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    }
}