from .base import *

# Debug
DEBUG = False

# Secret Key (for testing)
SECRET_KEY = 'test-secret-key'

# Database (in-memory SQLite for testing)
# Database (PostgreSQL for production)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
    }
}

