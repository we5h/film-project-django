from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import ContactForm
from .models import Contact


class ContactView(CreateView):
    model = Contact
    success_url = "/"
    fields = ['email',]
    template_name = 'contact/tags/form.html'