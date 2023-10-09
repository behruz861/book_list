from django import forms
from .models import Book
class GenreForm(forms.Form):
    name = forms.CharField(label='Genre Name')

