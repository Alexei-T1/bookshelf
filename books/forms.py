from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'author_full_name',
            'year_of_publishing',
            'copies_printed',
            'short_description',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'modal-form__input', 'placeholder': 'Название'}),
            'author_full_name': forms.TextInput(attrs={'class': 'modal-form__input', 'placeholder': 'Автор'}),
            'year_of_publishing': forms.NumberInput(attrs={'class': 'modal-form__input', 'placeholder': 'год публикации'}),
            'copies_printed': forms.NumberInput(attrs={'class': 'modal-form__input', 'placeholder': 'тираж'}),
            'short_description': forms.Textarea(attrs={'class': 'modal-form__input', 'rows': 4, 'placeholder': 'Описание'}),
        }
        labels = {
            'title': 'Название',
            'author_full_name': 'Автор',
            'year_of_publishing': 'Год издания',
            'copies_printed': 'Тираж',
            'short_description': 'Краткое описание',
        }