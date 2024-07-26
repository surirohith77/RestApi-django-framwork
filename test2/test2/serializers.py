from rest_framework import serializers
from .models import *


class CrickerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cricketers
        fields = ['id', 'name', 'role']


class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = ('file',)


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllUsers
        fields = ['id', 'firstName', 'lastName','mobile','password']


class LoginSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=10)
    password = serializers.CharField(max_length=50)