from django.urls import path
from . import views
# 
app_name = 'song-api'
urlpatterns = [
    path('get-list/',views.GetSongListApi.as_view(),name='songs'),
    path('get/<slug:slug>/',views.GetSongApi.as_view(),name='song'),
    path('get-artists/',views.GetArtistListApi.as_view(),name='artists'),
    path('get/artist/<slug:slug>/',views.GetArtistApi.as_view(),name='artist'),
    path('get-comming-songs/',views.GetCommingSoonSongsApi.as_view(),name='comming-soon'),
    path('vote-song/<int:pk>/',views.VoteSong.as_view(),name='vote'),
    path('pro-users/',views.ProUsersOnlyView.as_view(),name='pro-users'),

]