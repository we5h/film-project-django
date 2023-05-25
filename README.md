# Django_Movie project

Сервис хранения информации о фильмах, мультфильмах, сериалах, актеров и режиссеров.
На данном этапе находиться в СТАДИИ РАЗРАБОТКИ.

 Реализованы:
 - Пагинация
 - Фильтрация по жанрам и годам
 - Перевод страниц
 - Авторизация через VK (allauth)
 - Рассылка новостей и подписка через Celery(mail.ru smtp)
 - В админ панели установлен CKEditor

## Технологии проекта

**Lang:** Python 3.10

**Server:** Django 3.2


## Запуск проекта

Клонирование проекта

```bash
  git clone https://github.com/we5h/film-project-django
```

Переход в директорию проекта

```bash
  cd film-project-django
```

Установка зависимостей

```bash
  pip install -r requirements.txt
```

Запуск DEV сервера

```bash
  python film-project-django/django_movie/manage.py runserver
```

Установка, запуск Celery + Redis

Ставим Redis на Ubuntu:
```bash
curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg

echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list

sudo apt-get update
sudo apt-get install redis
```
```bash
sudo service redis-server start
```
Запуск Celery Worker:
```bash
celery -A django_movie worker -l info
```

## Автор

- Дмитрий Грибков [@we5h](https://www.github.com/we5h)