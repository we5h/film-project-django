from django.core.mail import send_mail


def send(user_email):
    send_mail(
        'Вы подписались на рассылку',
        'Мы будем присылать Вам много СПАМА :)',
        'the_bat_2015@mail.ru',
        [user_email],
        fail_silently=False,
    )