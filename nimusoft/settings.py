from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-0-6tlmcnc8%6r3rt936&si6n@5ehtcigu&$a-7bhad*ritms9t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#ALLOWED_HOSTS = ['localhost', 'nimusoft.com', 'www.nimusoft.com', 'env-nimusoft.eba-bartpuiq.us-west-2.elasticbeanstalk.com']
ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',
    
    # Local apps
    'home',
    'accounts',

    #3rd Party Apps
    'storages',
    
    'allauth',
    'allauth.account',
]

MIDDLEWARE = [
    
    # Django middleware
    'django.middleware.security.SecurityMiddleware',
    
    # Local middleware
    'whitenoise.middleware.WhiteNoiseMiddleware',
    
    # Django middleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'nimusoft.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'nimusoft.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


AUTH_USER_MODEL = 'accounts.CustomUser'

AUTHENTICATION_BACKENDS = (
    
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",

    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_UNIQUE_EMAIL = True

LOGIN_REDIRECT_URL = 'home:dashboard'
ACCOUNT_LOGOUT_REDIRECT_URL = '/accounts/login'

#Aws media storage

#media file storage class
#DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'



SITE_ID = 1
# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Dhaka'

USE_I18N = True

USE_TZ = True


#Static settings for development
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

#Static settings for production
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

#Media settings
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'


#CSRF_TRUSTED_ORIGINS = ['http://127.0.0.1:8000', 'https://nimusoft.com', 'https://www.nimusoft.com', 'https://env-nimusoft.eba-bartpuiq.us-west-2.elasticbeanstalk.com']

#secure ssl redirect
SECURE_SSL_REDIRECT = False

# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
