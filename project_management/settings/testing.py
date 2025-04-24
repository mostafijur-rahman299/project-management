from .base import *

# Debug
DEBUG = False

# Secret Key (for testing)
SECRET_KEY = 'test-secret-key'

# Database (in-memory SQLite for testing)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}
