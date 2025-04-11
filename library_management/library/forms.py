from django import forms
from .models import Book
from .models import Genre

class BookForm(forms.models.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'isbn', 'available_copies']

class BookSearchForm(forms.Form):
    query = forms.CharField(required=False, label='Search by title or author')
    genre = forms.ModelChoiceField(queryset=Genre.objects.all(), required=False, label='Genre')
    available = forms.BooleanField(required=False, label='Available only', initial=True)