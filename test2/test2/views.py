from django.http import JsonResponse
from .models import Cricketers
from .serializers import CrickerSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import FileUploadSerializer
from .serializers import UsersSerializer, LoginSerializer
from .models import AllUsers

@api_view(['GET', 'POST'])
def cricketList(request):
    if request.method == 'GET':
        cricket = Cricketers.objects.all()
        serializer = CrickerSerializer(cricket, many=True)

        # for json array
        # return JsonResponse(serializer.data,safe=False)

        # for json object
        return JsonResponse({"cricketers": serializer.data})

    if request.method == 'POST':
        serializer = CrickerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def cricketer_detail(request, id, format=None):
    try:
        cricketer = Cricketers.objects.get(pk=id)
    except Cricketers.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CrickerSerializer(cricketer)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CrickerSerializer(cricketer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cricketer.delete()
        return Response({"msg": "User Deleted Successfully"}, status=status.HTTP_200_OK)


class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = FileUploadSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def userRegisteration(request):
    if request.method == 'GET':
        print("GET request received")
        users = AllUsers.objects.all()
        print("Fetched users:", users)
        serializer = UsersSerializer(users, many=True)
        print("Serialized data:", serializer.data)
        return Response({"Users": serializer.data})

    if request.method == 'POST':
        print("POST request received")
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            print("Serializer is valid")
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print("Serializer errors:", serializer.errors)
            return Response({"msg": "Can't register now, please check your request"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        mobile = serializer.validated_data['mobile']
        password = serializer.validated_data['password']

        try:
            user = AllUsers.objects.get(mobile=mobile)
            if user.password == password:
                return Response({"msg": "Login successful"}, status=status.HTTP_200_OK)
            else:
                return Response({"msg": "Invalid password"}, status=status.HTTP_400_BAD_REQUEST)
        except AllUsers.DoesNotExist:
            return Response({"msg": "User does not exist"}, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


