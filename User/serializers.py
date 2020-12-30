from abc import ABC

from rest_framework import serializers
from User.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',
                  'name',
                  'phoneNo',
                  'password')


class UserLoginSerializer(serializers.Serializer):
    phoneNo = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=20)

    class Meta:
        fields = ('phoneNo', 'password')
