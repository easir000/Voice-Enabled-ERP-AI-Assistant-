from __future__ import absolute_import, unicode_literals
import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS__MODULE' , 'library_system.settings')

app = Celery('library_system')
app.config_from_object ('django.conf.settings' , namespace= 'CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'archive-old-books-every-30-minutes': {
        'task': 'api.tasks.archive-old-books',
        'schedule': 1800.0,
    },
}