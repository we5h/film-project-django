from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView

from .models import Movie, Category, Actor, Genre, Rating
from .forms import ReviewForm, RatingForm


class GenreYear:
    """Жанры и года выхода фильмов"""
    def get_genres(self):
        return Genre.objects.all()

    def get_years(self):
        return Movie.objects.filter(draft=False).values("year")


class MoviesView(GenreYear, ListView):
    """Список фильмов"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    paginate_by = 1

class MovieDetailView(GenreYear, DetailView):
    """Полное описание фильма"""
    model = Movie
    slug_field = "url"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)  # получаем словарь родителя и заносим его в переменную контекст
        context["categories"] = Category.objects.all()  # добавляем в словарь ключ категории и заносим туда queryset
        context["star_form"] = RatingForm()
        context["form"] = ReviewForm()
        return context


class AddReview(View):
    """Отзывы"""
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)  # Вызывая сейв, коммит фолс - хотим приостановить хранение нашей формы и можем внести изменения
            if request.POST.get('parent', None):  # Если в пост запросе есть пэрент - имя поля
                form.parent_id = int(request.POST.get('parent')) # Достаем значение ключа пэрент(оно строкове-оборачиваем в инт)
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())


class AddStarRating(View):
    """Добавление рейтинга фильму"""
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self,request):
        form = RatingForm(request.POST)
        if form.is_valid():
            Rating.objects.update_or_create(
                ip=self.get_client_ip(request),
                movie_id=int(request.POST.get("movie")),
                defaults={'star_id': int(request.POST.get("star"))}
            )
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)


class ActorView(GenreYear, DetailView):
    """Вывод информации об актере """
    model = Actor
    template_name = 'movies/actor.html'
    slug_field = "name"


class FilterMoviesView(GenreYear, ListView):
    """Фильтр фильмов"""
    paginate_by = 2

    def get_queryset(self):
        if 'genre' in self.request.GET and 'year' in self.request.GET:
            print('if genre and year')
            queryset = Movie.objects.filter(
            Q(year__in=self.request.GET.getlist("year")), Q(genres__in=self.request.GET.getlist("genre"))
            )
        else:
            print('else')
            queryset = Movie.objects.filter(
                Q(year__in=self.request.GET.getlist("year")) | Q(genres__in=self.request.GET.getlist("genre"))
            )
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["year"] = ''.join([f"year={x}&" for x in self.request.GET.getlist("year")])
        context["genre"] = ''.join([f"genre={x}&" for x in self.request.GET.getlist("genre")])
        return context