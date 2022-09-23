from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView

from .models import Movie
from .forms import ReviewForm


class MoviesView(ListView):
    """Список фильмов"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)


class MovieDetailView(DetailView):
    """Полное описание фильма"""
    model = Movie
    slug_field = "url"

class AddReview(View):
    """Отзывы"""
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)  # Вызывая сейв, коммит фолс - хотим приостановить хранение нашей формы и можем внести изменения
            if request.POST.get('parent', None): # Если в пост запросе есть пэрент - имя поля
                form.parent_id = int(request.POST.get('parent')) # Достаем значение ключа пэрент(оно строкове-оборачиваем в инт)
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())
