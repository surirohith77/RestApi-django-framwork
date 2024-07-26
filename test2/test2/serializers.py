from rest_framework import serializers
from .models import Cricketers
from .models import UploadedFile


class CrickerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cricketers
        fields = ['id', 'name', 'role']


class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = ('file',)