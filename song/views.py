from django.shortcuts import render,redirect
from django.views import View
from .models import Song
# Create your views here.

class SongListView(View):
    template_name ='song/songs.html'
    def get(self,request):
        songs = Song.objects.all()
        context = {'songs':songs}
        return render(request,self.template_name,context)
        # todo : search , paggination




