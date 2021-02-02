from django.http import HttpResponse
from django.http.response import JsonResponse
from django.http import QueryDict
from rest_framework import status, generics
import jwt
from rest_framework.views import APIView

from User.serializers import UserSerializer, UserLoginSerializer
from User.validator import check_user_exist
from . import fasade

# import internal modules
from . import mapper
from .models import User as UserModal


class UserDetails(generics.GenericAPIView):
    serializer_class = UserSerializer

    def put(self, request, id):
        try:
            user = check_user_exist(id)
            put = QueryDict(request.body)
            user_data = put.dict()
            user_serializer = UserSerializer(user, data=user_data)
            if user_serializer.is_valid():
                user_serializer.save()
                return JsonResponse(user_serializer.data)
            return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return HttpResponse(e)

    def delete(self, request, id):
        try:
            user = check_user_exist(id)
            user.delete()
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return HttpResponse(e)

    def get(self, request, id):
        try:
            user = check_user_exist(id)
            user_serializer = UserSerializer(user)
            return JsonResponse(user_serializer.data)
        except Exception as e:
            return HttpResponse(e)


class User(generics.CreateAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        user_data = request.POST.dict()
        # user_serializer = UserSerializer(data=user_data)
        user_serializer = self.get_serializer(data=request.data)
        if user_serializer.is_valid(raise_exception=True):
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Users(APIView):
    def get(self, request):
        users = UserModal.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)


class UserLogin(generics.CreateAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        user = request.POST.dict()
        fasade.login(user)
        user_data = UserModal.objects.all().filter(phoneNo=user.get('phoneNo'), password=user.get('password'))
        if user_data:
            user = {
                "username": user_data[0].name,
                "id": user_data[0].id
            }
            encoded_token = jwt.encode(user, 'SECRET', algorithm='HS256')
            return mapper.login(encoded_token)
        else:
            return JsonResponse('User not found', safe=False)
