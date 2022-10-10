from rest_framework.response import Response
from .serializers import *
from rest_framework import status
from rest_framework.views import APIView
from ..models import User
from song.models import Song,SongVote
from song.api.serializers import SongVoteSerializer
# 

class SignUpApi(APIView):
    def post(self,request):
        srz_data = SignUpApiSerializer(data=request.data)
        if srz_data.is_valid():
            srz_data.save()
            return Response(data=srz_data.data,status=status.HTTP_201_CREATED)
        return Response(srz_data.errors)


class ProfileApi(APIView):
    def get(self,request):
        fav_songs = SongVote.objects.filter(user=request.user)
        srz_data = SongVoteSerializer(fav_songs,many=True)
        return Response(data=srz_data.data)