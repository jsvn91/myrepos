import os
from django.core.wsgi import get_wsgi_application
from dj_static import Cling

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nirla.settings") #nirla is the name of the project

# added comment
# test added
application = Cling(get_wsgi_application())