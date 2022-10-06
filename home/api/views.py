from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ContactUsSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# 

class ContactUsApiView(APIView):
    """ users can request songs by filling this form and contact admins """
    permission_classes = [IsAuthenticated]
    serializer_class = ContactUsSerializer
    def post(self,request):
        srz_data = ContactUsSerializer(data = request.POST)
        if srz_data.is_valid():
            srz_data.create(srz_data.validated_data)
            return Response(srz_data.data, status=status.HTTP_201_CREATED)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)
    