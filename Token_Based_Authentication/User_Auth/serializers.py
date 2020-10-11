from rest_framework import serializers
from django.core.validators import validate_email
from rest_framework.validators import UniqueValidator
from .models import *

from .constants import *
from PIL import Image


class SignUpSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200, required=True)
    username = serializers.CharField(max_length=200, required=True)
    email = serializers.CharField(max_length=200, required=True)
    password = serializers.CharField(max_length=200, required=True)
    photo = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)

class EditProfileSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200, required=True)
    username = serializers.CharField(max_length=200, required=True)
    password = serializers.CharField(max_length=200, required=True)
    photo = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)
    expiry_window = serializers.IntegerField()



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=200, required=True)
    password = serializers.CharField(max_length=200, required=True)
    # if validate_email(email.value) is False:
    #     raise serializers.ValidationError(INVALID_EMAIL_FORMAT)

class APIResponseSerializer(serializers.Serializer):
    """
    Used for Serialization of APIResponse objects
    """
    status = serializers.IntegerField(required=True)
    message = serializers.CharField(required=True)
    data = serializers.JSONField(required=True)






