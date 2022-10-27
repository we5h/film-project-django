from django.core.mail import send_mail
from django_movie.celery import app
from .service import send, send_news
from .models import Contact


@app.task
def send_spam_email(user_email):
    send(user_email)


@app.task
def send_beat_email():
   send_news()