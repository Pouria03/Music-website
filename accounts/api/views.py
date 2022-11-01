from rest_framework.response import Response
from .serializers import *
from rest_framework import status
from rest_framework.views import APIView
from ..models import User
from song.models import Song,SongVote
from song.api.serializers import SongVoteSerializer
# 

class SignUpApi(APIView):
    ''' register user in system '''
    serializer_class = SignUpApiSerializer
    def post(self,request):
        srz_data = self.serializer_class(data=request.data)
        if srz_data.is_valid():
            srz_data.save()
            return Response(data=srz_data.data,status=status.HTTP_201_CREATED)
        return Response(srz_data.errors)


class ProfileApi(APIView):
    ''' user's favorite songs '''
    serializer_class = SongVoteSerializer
    def get(self,request):
        fav_songs = SongVote.objects.filter(user=request.user)
        srz_data = self.serializer_class(fav_songs,many=True)
        return Response(data=srz_data.data,status=status.HTTP_200_OK)

