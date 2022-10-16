import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_movie.settings')  # пути для настроек брокеров в дальнейшем

app = Celery('django_movie')
app.config_from_object('django.conf:settings', namespace='CELERY')  # переменные, которые будут начинаться с CELERY, будет прочитывать и подцеплять к себе
app.autodiscover_tasks()  # автоматически подцеплять таски в приложениях



# celery beat tasks

app.conf.beat_schedule = {
    'send-spam-every-5-minute': {
        'task': 'contact.tasks.send_beat_email',
        'schedule': crontab(minute='*/5'),  # */5 каждые 5 мин
    }
}