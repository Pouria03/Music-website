from django.urls import path
from . import views

app_name = 'song'
urlpatterns = [
    path('songs/',views.SongListView.as_view(),name='list'),
    path('song/<int:pk>/<slug:slug>/',views.GetSongView.as_view(),name='detail'),
    path('artists/',views.ArtistListView.as_view(),name='artists'),
    path('artist/<slug:slug>/',views.GetArtistView.as_view(),name='artist'),
    # path('category/<slug:slug>/'views.GetCategoryView.as_view(),name='category')
    
]