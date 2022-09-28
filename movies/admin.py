from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms
from .models import *

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class MovieAdminForm(forms.ModelForm):  # виджет для загрузки изображений CKEditor(отдельная установка в django pip)
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Movie
        fields = '__all__'



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
    list_display_links = ('name',)


class ReviewInLine(admin.TabularInline):  # появляются отзывы под выбранным фильмом внизу в линию Tabular - горизонтально
    model = Reviews
    extra = 1  # количество отображаемых отзывов
    readonly_fields = ("name", "email",)


class MovieShotsInLine(admin.TabularInline):  # появляются кадры из фильма при редактировании фильма + необходимо добавить в класс MovieAdmin
    model = MovieShots
    extra = 1
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110"')

    get_image.short_description = 'Кадр из фильма'


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    '''Фильмы'''
    list_display = ('title', 'category', 'url', 'draft', )
    list_filter = ('category', 'year',)
    search_fields = ('title', 'category__name',)  # чтобы искать по категории надо указать по какому полю категории будем искать
    inlines = [MovieShotsInLine, ReviewInLine]  # подключаем классы для отзывов и кадров внизу фильма
    actions = ['unpublish', 'publish']
    save_on_top = True  # кнопки сохранения сверху
    save_as = True  # добавляется поле 'Сохранить как новый объект'
    list_editable = ('draft',)  # поле черновик сделали "галочкой" - редактируемым
    form = MovieAdminForm  # поле для редактирования - CKEditor
    readonly_fields = ('get_image',)
    fieldsets = [    # поля в одну строку (кортеж в кортеже)
        (None, {
            "fields": (('title', 'tagline', ), )
        }),
        (None, {
            "fields": ('description', ('poster', 'get_image',),)
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

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="100" height="110"')

    def unpublish(self, request, queryset):  # экшен
        """Снять с публикации"""
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        elif row_update == 2 or row_update == 3 or row_update == 4:
            message_bit = f"{row_update} записи были обновлены"
        else:
            message_bit = f"{row_update} записей было обновлено"
        self.message_user(request, f"{message_bit}")

    def publish(self, request, queryset):
        """Опубликовать"""
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        elif row_update == 2 or row_update == 3 or row_update == 4:
            message_bit = f"{row_update} записи были обновлены"
        else:
            message_bit = f"{row_update} записей было обновлено"
            self.message_user(request, f"{message_bit}")

    unpublish.short_description = "Снять с публикации"
    unpublish.allowed_permission = ('change',)  # права пользователя на изменения записи

    publish.short_description = "Опубликовать"
    publish.allowed_permission = ('change', )

    get_image.short_description = 'Постер'


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
    list_display = ("name", "age", "get_image")
    readonly_fields = ("get_image",)  # будет отображаться в окне, где можно изменить объект

    def get_image(self, obj):  # делаем миниатюру изображения в админке, обязательно передать в list_display
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')  # выведет HTML не как строку,а как тэг

    get_image.short_description = 'Изображение'  # так будет называться столбец

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """Рейтинг"""
    list_display = ("star", "ip")


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    """Кадры из фильма"""
    list_display = ("title", "movie", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = 'Кадр из фильма'

admin.site.register(RatingStar)

admin.site.site_title = 'Django Movies'
admin.site.site_header = 'Django Movies'