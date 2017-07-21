from rest_framework import serializers
from rest_framework.serializers import Serializer, ModelSerializer

from .models import User


class HelloSerializer(Serializer):

    name = serializers.CharField(max_length=10)


class UserProfileSerializer(ModelSerializer):
    '''A serializer for user profile object'''
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def create(self, validated_data):
        '''create and return a new user'''
        user = User(
            email=validated_data.get('email'),
            name=validated_data.get('name')
        )
        user.set_password(validated_data.get('password'))
        user.save()
        return user
