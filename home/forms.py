from song.models import (Song,Category,Artist)
from django import forms
# 

class SearchForm(forms.Form):
    search = forms.CharField()


class ContactUsForm(forms.Form):
    contact_type = forms.CharField()
    request = forms.CharField()
