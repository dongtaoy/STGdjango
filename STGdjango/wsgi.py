"""
WSGI config for STGdjango project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os,sys
sys.path.append('/home/stg/STGdjango')
os.environ["DJANGO_SETTINGS_MODULE"] = "STGdjango.settings"
os.environ['PYTHON_EGG_CACHE'] = '/tmp/.python-eggs'
from django.contrib.auth.handlers.modwsgi import check_password
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
