from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *


class MenAPIView(APIView):
    def get(self, request):
        lst = Men.objects.all().values()
        return Response({'posts': list(lst)})
    
    def post(self, request):
        return Response({'Zurab': 'Tigr'})

# class MenAPIView(generics.ListAPIView):
#     queryset = Men.objects.all()
#     serializer_class = MenSeralzer