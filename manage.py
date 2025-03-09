#!/usr/bin/env python
import os
import sys
from dotenv import load_dotenv  # Pour les variables d'.env
# Prendre les variables d'environnement
load_dotenv()
if not os.getenv("DEPLOY_DEV_OR_PRODUCTION") in ("dev", "production"):
    raise ValueError("DEPLOY_DEV_OR_PRODUCTION %s doit etre dev ou production" % os.getenv("DEPLOY_DEV_OR_PRODUCTION"))

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.%s" % os.getenv("DEPLOY_DEV_OR_PRODUCTION") )

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
