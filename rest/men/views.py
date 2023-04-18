from django.shortcuts import render
from django.forms import model_to_dict
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *


class MenAPIView(APIView):
    def get(self, request):
        m = Men.objects.all()
        return Response({'posts': MenSerializer(m, many=True).data})
    
    def post(self, request):
        serializer = MenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})
    
    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "method PUT not allwed"})
        try:
            instance = Men.objects.get(pk=pk)
        except:
            return Response({"error": "objects does not exists"})
        
        serializer = MenSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})
    
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "method PUT not allwed"})


        

# class MenAPIView(generics.ListAPIView):
#     queryset = Men.objects.all()
#     serializer_class = MenSeralzer