from rest_framework import serializers
from ..models import ContactUs
#
class ContactUsSerializer(serializers.Serializer):
    contact_type = serializers.CharField()
    request = serializers.CharField()
    
    def create(self,validated_data):
        return ContactUs.objects.create(**validated_data)

    