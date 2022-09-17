from django.urls import path
from . import views

app_name = 'song'
urlpatterns = [
    path('songs/',views.SongListView.as_view(),name='list'),
#     path('song/<pk:pk>/<slug:slug>/',views.GetSongView.as_views(),name='detail'),
#     path('artists/',views.ArtistsView.as_view(),name='artists'),
#     path('artist/<slug:slug>/',views.GetArtistView.as_view(),name='artist'),
#     path('categories/',views.CategoriesView.as_view(),name='categories'),
#     path('category/<slug:slug>/'views.GetCategoryView.as_view(),name='category')
    
]