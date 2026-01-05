import os
import sys
from django.core.wsgi import get_wsgi_application

path = '/home/USERNAME/MRHMS'
if path not in sys.path:
    sys.path.append(path)

activate_this = '/home/USERNAME/MRHMS/.venv/bin/activate_this.py'
with open(activate_this) as f:
    exec(f.read(), {'__file__': activate_this})

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mrhms.settings')
application = get_wsgi_application()

