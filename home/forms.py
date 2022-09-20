from song.models import (Song,Category,Artist)
from django import forms

class SearchForm(forms.Form):
    search = forms.CharField()
