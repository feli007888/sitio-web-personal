import os
import sys

# Ruta a la carpeta de tu proyecto
path = '/home/feli007888/sitio-web-personal'
if path not in sys.path:
    sys.path.append(path)

# Apunta al archivo settings de tu carpeta 'sitio'
os.environ['DJANGO_SETTINGS_MODULE'] = 'sitio.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
