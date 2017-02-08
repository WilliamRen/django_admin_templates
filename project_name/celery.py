from __future__ import absolute_import
import os
from celery import Celery

PWD = os.path.dirname(os.path.abspath(__file__))
APP = os.path.basename(PWD)

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', '%s.settings' % APP)

from django.conf import settings

app = Celery(APP)

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True, name=u"celery debug")
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
