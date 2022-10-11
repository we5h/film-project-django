from django.db import models

class Contact(models.Model):
    """Подписка на email"""
    email = models.EmailField()
    date = models.DateTimeField(auto_now=True)  # автоматически заполняется при создании записи

    def __str__(self):
        return self.email
