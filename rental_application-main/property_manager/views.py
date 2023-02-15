from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Property
from rest_framework import status
from .serializer import propertyserializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class propertypost(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Property.objects.get(pk=pk)
        except Property.DoesNotExist:
            return Response("not valid")

    # list all get data from the table
    def get(self, request, format=None):
        property_details = Property.objects.all()
        serializer = propertyserializer(property_details)
        return Response(serializer.data, status=status.HTTP_302_FOUND)

    def post(self, request, format=None):
        property_details = request.data
        serializer = propertyserializer(data=property_details)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        data = self.get_object(pk)
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
