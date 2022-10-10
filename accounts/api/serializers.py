from dataclasses import fields
from rest_framework import serializers
from ..models import User
# 

class SignUpApiSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['email','password']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 4}}


    def create(self, validated_data):
        return User.objects.create_user(email=validated_data['email'],password=validated_data['password'])
