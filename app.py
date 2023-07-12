import os
from django.core.wsgi import get_wsgi_application
from mysite.wsgi import application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_wsgi_application()


app = application