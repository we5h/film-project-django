from modeltranslation.translator import register, TranslationOptions
from .models import Category, Actor, Movie, Genre, MovieShots


@register(Category)
class CategoryTranslationOption(TranslationOptions):
    fields = ('name', 'description')


@register(Actor)
class ActorTranslationOption(TranslationOptions):
    fields = ('name', 'description')


@register(Genre)
class GenreTranslationOption(TranslationOptions):
    fields = ('name', 'description')


@register(Movie)
class MovieTranslationOption(TranslationOptions):
    fields = ('title', 'description', 'tagline', 'country')


@register(MovieShots)
class MovieTranslationOption(TranslationOptions):
    fields = ('title', 'description')