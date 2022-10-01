from django import forms

from .models import Reviews, Rating, RatingStar


class ReviewForm(forms.ModelForm):
    '''Форма отзыва'''
    class Meta:
        model = Reviews
        fields = ('name', 'email', 'text')


class RatingForm(forms.ModelForm):
    """Форма добавления рейтинга"""
    star = forms.ModelChoiceField(
        queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None  # виджет - это то,как будет представлена форма в HTML
    )

    class Meta:
        model = Rating
        fields = ("star", )