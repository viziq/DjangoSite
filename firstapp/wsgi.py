import os
import sys

# add your project directory to the sys.path
project_home = u'/home/viziq/project/bin/firstapp'
if project_home not in sys.path:
    sys.path.append(project_home)

# set environment variable to tell django where your settings.py is
os.environ['DJANGO_SETTINGS_MODULE'] = 'firstapp.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
