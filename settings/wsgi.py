"""
WSGI config for gvcoop project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from dotenv import load_dotenv  # Pour les variables d'.env
from django.core.wsgi import get_wsgi_application
# Prendre les variables d'environnement
load_dotenv()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.%s" % os.getenv("DEPLOY_DEV_OR_PRODUCTION"))

application = get_wsgi_application()
