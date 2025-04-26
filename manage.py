#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from decouple import config


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_management.settings.base')
    # Check if the environment variable is set to 'production'
    if config('DJANGO_ENV') == 'production':
        os.environ['DJANGO_SETTINGS_MODULE'] = 'project_management.settings.production'
    elif config('DJANGO_ENV') == 'development':
        os.environ['DJANGO_SETTINGS_MODULE'] = 'project_management.settings.development'
    elif config('DJANGO_ENV') == 'testing':
        os.environ['DJANGO_SETTINGS_MODULE'] = 'project_management.settings.testing'
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
