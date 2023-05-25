from django.core.mail import send_mail

from movies.models import Movie
from .models import Contact


def send(user_email):
    send_mail(
        'Вы подписались на рассылку',
        'Мы будем присылать Вам много СПАМА :)',
        'the_bat_2015@mail.ru',
        [user_email],
        fail_silently=False,
    )


def send_news():
    movies = Movie.objects.order_by("-id")[:5]
    novelties = [movie.title for movie in movies]

    for contact in Contact.objects.all():
        send_mail(
            'Новинки на нашем сайте Django-Movies для тебя!',
            'Привет,друг! Мы рады сообщить тебе, что у нас на портале появились'
            ' новые фильмы!'
            '{}'.format(', '.join(map(str, novelties))),
            'the_bat_2015@mail.ru',
            [contact.email],
            fail_silently=False,
        ),