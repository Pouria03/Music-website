from song.models import Song,Artist
from django.db.models import Q
# search module
def search(request,queryset):
    if request.GET.get('search'):
        q = request.GET.get('search')

        if queryset.model is Song:
            queryset = queryset.filter(Q(title__icontains=q) | Q(lyrics__icontains=q) | 
            Q(artist__name__icontains=q))
        if queryset.model is Artist:
            queryset = queryset.filter(name__icontains=q)
    return queryset