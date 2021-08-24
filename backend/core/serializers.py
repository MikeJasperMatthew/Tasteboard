from django.db.models import fields
from rest_framework import serializers
from core.models import *


#core serializer
class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'