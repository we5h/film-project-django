from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
    list_display_links = ('name',)


class ReviewInLine(admin.TabularInline):  # появляются отзывы под выбранным фильмом внизу в линию Tabular - горизонтально
    model = Reviews
    extra = 1  # количество отображаемых отзывов
    readonly_fields = ("name", "email",)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url', 'draft',)
    list_filter = ('category', 'year',)
    search_fields = ('title', 'category__name',)  # чтобы искать по категории надо указать по какому полю категории будем искать
    inlines = [ReviewInLine]  # подключаем класс для отзывов внизу фильма
    save_on_top = True  # кнопки сохранения сверху
    save_as = True  # добавляется поле 'Сохранить как новый объект'
    list_editable = ('draft',)  # поле черновик сделали "галочкой" - редактируемым
    fieldsets = [    # поля в одну строку (кортеж в кортеже)
        (None, {
            "fields": (('title', 'tagline'), )
        }),
        (None, {
            "fields": (('description', 'poster'),)
        }),
        (None, {
            "fields": (('year', 'world_premiere', 'country'),)
        }),
        ("Actors", {
            "classes": ('collapse',),
            "fields": (('actors', 'directors', 'genres', 'category'),)
        }),
        (None, {
            "fields": (('budget', 'fees_in_usa', 'fees_in_world'),)
        }),
        ("Options", {
            "fields": (('url', 'draft', ),)
        }),
    ]


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'parent', 'movie', 'id')
    readonly_fields = ('name', 'email',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Жанры"""
    list_display = ("name", "url")


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    """Актеры"""
    list_display = ("name", "age")


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """Рейтинг"""
    list_display = ("star", "ip")


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    """Кадры из фильма"""
    list_display = ("title", "movie")


admin.site.register(RatingStar)
