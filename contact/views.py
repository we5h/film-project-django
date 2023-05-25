from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import ContactForm
from .models import Contact
from .service import send
from .tasks import send_spam_email

class ContactView(CreateView):
    model = Contact
    success_url = "/"
    fields = ['email', ]
    template_name = 'contact/tags/form.html'

    def form_valid(self, form):
        form.save()
        # send(form.instance.email)
        send_spam_email.delay(form.instance.email)
        return super().form_valid(form)