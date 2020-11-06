#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trial_proj.settings')
    # CUSTOM CODE FOR AUTOMATIC IMPORTATION OF SECRETS ON WINDOWS SYSTEMS #
    if sys.platform == "win32":
        try:
            with open(os.path.join(os.path.dirname(__file__), "secrets.txt")) as f:
                for line in f:
                    temp = line.split("=")
                    os.environ[temp[0]] = temp[1].replace('"', '').strip()
        except FileNotFoundError:
            print(f'No secrets file found in: "{os.getcwd()}"')
    # END CUSTOM #
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
