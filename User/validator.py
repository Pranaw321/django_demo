from User.models import User
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.views import exception_handler
from rest_framework.response import Response
from public.helper import custom_exception_handler


def check_user_exist(id):
    try:
        user = User.objects.get(id=id)
        return user
    except User.DoesNotExist:
        raise Exception("This user does not exist", status.HTTP_404_NOT_FOUND)
