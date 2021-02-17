from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from apps.config.settings import CELERY_BROKER_URL, CELERY_RETRY_DELAY, CELERY_RETRY_MAX_TIMES

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'apps.config.settings')

# Setup celery
celery_app = Celery('workshop-django', broker=CELERY_BROKER_URL)

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
celery_app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
celery_app.autodiscover_tasks()

# This will make sure the app is always imported when Django starts so that shared_task will use this app.
__all__ = ('celery_app', CELERY_RETRY_DELAY, CELERY_RETRY_MAX_TIMES)
