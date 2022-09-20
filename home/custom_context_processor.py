from song.models import (Song,Category,Artist)
from .forms import SearchForm

def search(request):
    return {'search_form' : SearchForm}