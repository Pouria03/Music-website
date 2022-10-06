from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from .models import Song,Artist,Category,SongVote
from utils import search
from accounts.models import User
# Create your views here.

class SongListView(View):
    template_name ='song/list.html'
    page_title = 'songs'
    def get(self,request,page=1):
        songs = Song.objects.all()
        songs = search.search(request,queryset=songs)
        # paggination
        paginator = Paginator(songs,6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        # end of paggination
        context = {'songs':page_obj,'page_title':self.page_title}
        return render(request,self.template_name,context)
    # todo : paggination

class GetSongView(View):
    template_name = 'song/detail.html'
    def get(self,request,*args,**kwargs):
        pk = kwargs.get('pk')
        slug = kwargs.get('slug')
        song = get_object_or_404(Song,pk=pk,slug=slug)
        context = {'song':song}
        return render(request,self.template_name,context)


class ArtistListView(View):
    template_name = 'song/artists.html'
    page_title = 'artists'
    def get(self,request):
        artists = Artist.objects.all()
        artists = search.search(request,queryset=artists)
        # paggination
        paginator = Paginator(artists,6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        # end of paggination          
        context = {'artists': page_obj,'page_title':self.page_title}
        return render(request,self.template_name,context)

class GetArtistView(View):
    template_name = 'song/artist_page.html'
    page_title = 'artist profile'
    def get(self,request,slug):
        artist = get_object_or_404(Artist,slug=slug)
        artist_songs = Song.objects.filter(artist__name = artist.name)
        context = {'artist': artist,'page_title':self.page_title,'artist_songs':artist_songs}
        return render(request,self.template_name,context)


class VoteView(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('song:list')
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,song_id):
        song = Song.objects.get(id=song_id)
        vote = SongVote.objects.filter(user=request.user ,song=song)
        if vote.exists():
            vote.delete()
            messages.success(request,'you unvoted the song','success')
            return redirect('song:detail',song.id,song.slug)
        elif not vote.exists():
            SongVote.objects.create(user=request.user,song=song).save()
            messages.success(request,'you voted the song','success')
        return redirect('song:detail',song.id,song.slug)


class CommingSoonSongsView(View):
    template_name = 'song/commingsoon.html'
    def get(self,request):
        comming_soon_songs = Song.objects.filter( Q(file='') | Q(file__isnull=True))
        comming_soon_songs = search.search(request,queryset=comming_soon_songs)
        context= {'comming_soon_songs':comming_soon_songs}
        return render(request,self.template_name,context)




        
class ProUsersClass(View):
    template_name = 'song/pro_users.html'
    def dispatch(self, request, *args, **kwargs):
        users = User.objects.filter(groups__name='premium_users')
        if not request.user in users :
            messages.warning(request,'BANN','warning')
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)
    def get(self,request):
        return render(request,self.template_name)