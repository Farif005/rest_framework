from rest_framework import serializers
from .models import *


class MenSeralzer(serializers.ModelSerializer):
    class Meta:
        model = Men
        fields = ('title', 'cat_id')