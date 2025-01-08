import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "KinoMir.settings")

app = Celery("KinoMir")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
