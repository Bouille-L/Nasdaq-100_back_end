#!/usr/bin/env python
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nasdaq_100_ETF_Explorer.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    # Check if process.env.PORT is set
    if os.environ.get('PORT'):
        # If PORT is set, default binding to '0.0.0.0'
        sys.argv.insert(2, '0.0.0.0:8000')
    
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
