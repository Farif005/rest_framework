from django.shortcuts import render
from django.forms import model_to_dict
from rest_framework import generics, viewsets
from rest_framework.permissions import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from .permissions import *
from .serializers import *
from .models import *


# class MenViewSet(viewsets.ModelViewSet):
#     # queryset = Men.objects.all()
#     serializer_class = MenSerializer

#     def get_queryset(self):
#         pk = self.kwargs.get("pk")

#         if not pk:
#             return Men.objects.all()[:3]
        
#         return Men.objects.filter(pk=pk)

#     @action(methods=['get'], detail=False)
#     def category(self, request):
#         cats = Category.objects.all()
#         return Response({'cats': [c.name for c in cats]})



class MenAPIList(generics.ListCreateAPIView):
    queryset = Men.objects.all()
    serializer_class = MenSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

class MenAPIUpdate(generics.UpdateAPIView):
    queryset = Men.objects.all()
    serializer_class = MenSerializer
    permission_classes = (IsOwnerOrReadOnly,)

class MenAPIDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Men.objects.all()
    serializer_class = MenSerializer
    permission_classes = (IsAdminOrReadOnly, )



# class MenAPIView(APIView):
#     def get(self, request):
#         m = Men.objects.all()
#         return Response({'posts': MenSerializer(m, many=True).data})
    
#     def post(self, request): # проверить работу
#         serializer = MenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response({'post': serializer.data})
    
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "method PUT not allwed"})
#         try:
#             instance = Men.objects.get(pk=pk)
#         except:
#             return Response({"error": "objects does not exists"})
        
#         serializer = MenSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})
    
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "method PUT not allwed"})
        
#         Men.objects.delete(pk=pk)
        
#         return Response({"post": "delete post" + str(pk)})


        

# class MenAPIView(generics.ListAPIView):
#     queryset = Men.objects.all()
#     serializer_class = MenSeralzer