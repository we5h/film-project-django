from django.db import models
from django.utils.translation import ugettext_lazy as _

class Contact(models.Model):
    """Подписка на email"""
    email = models.EmailField()
    date = models.DateTimeField(auto_now=True)  # автоматически заполняется при создании записи

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _("Email для рассылок")
        verbose_name_plural = _("Email для рассылок")
