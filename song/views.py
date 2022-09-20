from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from django.db.models import Q
from django.views import View
from .models import Song,Artist,Category,SongVote
# Create your views here.

class SongListView(View):
    template_name ='song/list.html'
    page_title = 'songs'
    def get(self,request):
        songs = Song.objects.all()
        if request.GET.get('search'):
            q = request.GET.get('search')
            songs = songs.filter( Q(title__icontains=q)
             | Q(lyrics__icontains=q) 
             | Q(artist__name__icontains=q))
        context = {'songs':songs,'page_title':self.page_title}
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

        if request.GET.get('search'):
            q = request.GET.get('search')
            artists = artists.filter(name__icontains=q)
            
        context = {'artists': artists,'page_title':self.page_title}
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