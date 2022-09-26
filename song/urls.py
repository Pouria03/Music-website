from django.urls import path
from . import views

app_name = 'song'
urlpatterns = [
    path('songs/',views.SongListView.as_view(),name='list'),
    path('song/<int:pk>/<slug:slug>/',views.GetSongView.as_view(),name='detail'),
    path('artists/',views.ArtistListView.as_view(),name='artists'),
    path('artist/<slug:slug>/',views.GetArtistView.as_view(),name='artist'),
    path('vote/<int:song_id>/',views.VoteView.as_view(),name='vote'),
    path('comming-soon/',views.CommingSoonSongsView.as_view(),name='comming-soon'),
    path('prousers/',views.ProUsersClass.as_view())
    # path('category/<slug:slug>/'views.GetCategoryView.as_view(),name='category')
    
]