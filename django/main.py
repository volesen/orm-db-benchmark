import os
import django

# Django specific settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

# Django 
django.setup()

# Application specific imports
from data.models import *

