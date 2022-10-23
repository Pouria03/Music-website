from dataclasses import fields
from rest_framework import serializers
from ..models import *
# 

# favorite songs
class SongVoteSerializer(serializers.ModelSerializer):
    song = serializers.StringRelatedField()
    class Meta:
        model = SongVote
        fields = ('song',)

# song list
class SongSerializer(serializers.ModelSerializer):
    artist = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    class Meta:
        model = Song
        fields = ('id','artist','category','title','slug','description',
        'image','file','lyrics','created_time')


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('name','slug')
