from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from clasificador_api import serializer
# Create your views here.

class HelloApiView(APIView):
    """"""
    serializer_class = serializer.HelloSerializer
    def post(self, request):
        """"""
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        an_apiview = [
        'Uses HTTP methods as function (get, post, patch, put, delete)',
        'Is similar to a traditional Django View',
        'Gives you the most control over your logic',
        'Is mapped manually to URLs',
        ]
        
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})