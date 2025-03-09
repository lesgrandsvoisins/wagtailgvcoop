from allauth.account.signals import user_signed_up
from django.contrib.auth.models import Group

from .base import *

import settings.secrets.lesecret

import os

DEBUG = False

if "SECRET_KEY" in os.environ:
    SECRET_KEY = os.environ["SECRET_KEY"]

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "*").split(",")

if "CSRF_TRUSTED_ORIGINS" in os.environ:
    CSRF_TRUSTED_ORIGINS = os.environ["CSRF_TRUSTED_ORIGINS"].split(",")

try:
    from .local import *
except ImportError:
    pass
