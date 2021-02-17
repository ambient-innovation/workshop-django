import datetime
import logging

from django.conf import settings
from django.db import connections
from django.utils.translation import gettext as _
from django_db_logger.models import StatusLog
from pytz import utc

from apps.config.celery_settings import celery_app


@celery_app.task
def clear_sessions():
    from django.core.management import call_command

    logger = logging.getLogger('system')
    logger.info(_('Alte Sessioneinträge aufgeräumt.'))

    call_command('clearsessions')


@celery_app.task
def remove_old_system_logs():
    # Log action
    logger = logging.getLogger('system')

    # Border: X days ago (-> settings.py)
    debug_border = utc.localize(datetime.datetime.today() -
                                datetime.timedelta(days=(settings.DB_LOGGER_ENTRY_LIFETIME / 3)))
    info_border = utc.localize(datetime.datetime.today() -
                               datetime.timedelta(days=settings.DB_LOGGER_ENTRY_LIFETIME))

    debug_logs = StatusLog.objects.filter(level__lte=logging.DEBUG, create_datetime__lte=debug_border)
    other_logs = StatusLog.objects.filter(level__gt=logging.DEBUG, create_datetime__lte=info_border)

    logger.info(_(f'{debug_logs.count()} Debug-Logeinträge gelöscht.'))
    logger.info(_(f'{other_logs.count()} Logeinträge gelöscht.'))

    debug_logs.delete()
    other_logs.delete()

    cursor = connections['default'].cursor()
    cursor.execute('OPTIMIZE TABLE django_db_logger_statuslog;')
