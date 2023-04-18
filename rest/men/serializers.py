from rest_framework import serializers
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import *


# class MenModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content
        

class MenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()

    def create(self, validated_data):
        return Men.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.content = validated_data.get("content", instance.content)
        instance.time_update = validated_data.get("time_update", instance.time_update)
        instance.is_published = validated_data.get("is_published", instance.is_published)
        instance.cat_id = validated_data.get("cat_id", instance.cat_id)
        instance.save()
        return instance


# def encode():
#     model = MenModel('Bred', 'Pitt')
#     model_sr = MenSeralzer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)

# def decode():
#     stream = io.BytesIO(b'{"title":"Bred","content":"Pitt"}')
#     data = JSONParser().parse(stream)
#     serializers = MenSeralzer(data=data)
#     serializers.is_valid()
#     print(serializers.validated_data)