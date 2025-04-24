from .base import *

# Debug
DEBUG = True

# Secret Key (for development only)
SECRET_KEY = 'django-insecure-your-development-secret-key'

# Allowed Hosts
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Database (SQLite for development)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
