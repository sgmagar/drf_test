from rest_framework import serializers
from rest_framework.serializers import Serializer, ModelSerializer

from .models import User, ProfileFeedItem


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
            name=validated_data.get('name'),
            username=validated_data.get('name')
        )
        user.set_password(validated_data.get('password'))
        user.save()
        return user


class ProfileFeedItemSerializer(ModelSerializer):
    '''A serializer for profile feed items'''

    class Meta:
        model = ProfileFeedItem
        fields = ('id', 'user', 'status_text', 'created_on')
        extra_kwargs = {
            'user': {
                'read_only': True
            }
        }
