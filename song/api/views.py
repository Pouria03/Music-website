from rest_framework.views import APIView
from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from .serializers import *
from ..models import *
from utils.custom_permissions import IsProUser
# 

class GetSongListApi(APIView):
    """ this api is to display a list of songs """
    serializer_class = SongSerializer
    def get(self,request):
        songs = Song.objects.all()
        srz_data = self.serializer_class(songs,many=True)
        return Response(data=srz_data.data,status=status.HTTP_200_OK)


class GetSongApi(APIView):
    """ this api is to display a details of a song """
    serializer_class = SongSerializer
    def get(self,request,slug):
        song = Song.objects.get(slug=slug)
        srz_data = self.serializer_class(song)
        return Response(srz_data.data,status=status.HTTP_200_OK)


class GetArtistListApi(APIView):
    """ this api is to display list of artists """
    serializer_class = ArtistSerializer
    def get(self,request):
            artists =  Artist.objects.all()
            srz_data = self.serializer_class(artists,many=True) 
            return Response(data=srz_data.data,status=status.HTTP_200_OK)

class GetArtistApi(APIView):
    """ this api is to display details of an artist """
    serializer_class = ArtistSerializer
    def get(self,request,slug):
        artist = Artist.objects.get(slug=slug)
        srz_data = self.serializer_class(artist) 
        return Response(srz_data.data,status=status.HTTP_200_OK)


class GetCommingSoonSongsApi(APIView):
    """ this api is to display list of up comming songs """
    serializer_class = SongSerializer
    def get(self,request):
        comming_songs = Song.objects.filter( Q(file='') | Q(file__isnull=True))
        srz_data = self.serializer_class(comming_songs,many=True)
        return Response(data=srz_data.data,status=status.HTTP_200_OK)


class VoteSong(APIView):
    """ this api is to vote a song or to Unvote a voted song"""
    serializer_class = SongVoteSerializer
    def post(self,request,pk):
        song = Song.objects.get(pk=pk)
        vote = SongVote.objects.filter(song=song,user=request.user)
        if vote.exists():
            vote.delete()
            data = {'message':'you unvoted this song'}
            return Response(data=data,status=status.HTTP_200_OK)
        else :
            SongVote.objects.create(song=song,user=request.user)
            data = {'message':'you voted this song'}
            return Response(data=data,status=status.HTTP_201_CREATED)


class ProUsersOnlyView(APIView):
    """ only premium uesers can enter"""
    message = 'ACCESS DENIED'
    permission_classes = [IsProUser]
    def get(self,request):
        data = {'msg':'comming soon'}
        return Response(data,status=status.HTTP_401_UNAUTHORIZED)