"""
WSGI config for blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')
#sys.path.append('/home/usher/django/blog')
sys.path.append('/mnt/django/blog')
application = get_wsgi_application()
#def application(environ, start_response):
#    start_response('200 OK', [('Content-Type','text/html')])
#    return [b"Hello World"]
