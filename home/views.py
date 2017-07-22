# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .models import User, ProfileFeedItem

from .serializers import HelloSerializer, UserProfileSerializer, ProfileFeedItemSerializer
from .permissions import UpdateOwnprofile, PostOwnStatus


class HelloApiView(APIView):

    serializer_class = HelloSerializer

    def get(self, request, format=None):
        an_apiview = [
            'It is like a traditinal django view,',
            'Give you control over logic.',
            'Is mapped to url.'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {}'.format(name)
            return Response({'message': message})

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        '''Handles updating an object'''

        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        '''partially update an object'''
        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        'Deletes an object'
        return Response({'method': 'delete'})


class HelloViewSet(ViewSet):
    '''Test Api View Set'''
    serializer_class = HelloSerializer

    def list(self, request):
        a_viewset = [
            'Uses actions (list, create, retreive, update, partially update)',
            'Automaticatlly maps to URLS using Routers',
            'Provides more functionality with less code.'
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        '''create a new hello message'''
        serializer = HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {}'.format(name)
            return Response({'message': message})
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        '''handles getting an object by id'''
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        '''handles updating an object'''
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        '''handles updating part of an object'''
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        '''handles removing an object'''
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = User.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnprofile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')


class LoginViewSet(ViewSet):
    '''Check email and password and returns an auth token'''

    serializer_class = AuthTokenSerializer

    def create(self, request):
        '''use ObtainAuthToken APIView to validate and create a token'''
        return ObtainAuthToken().post(request)


class UserProfileFeedViewSet(ModelViewSet):
    '''handle add, create, delete profile feed items'''
    authentication_classes = (TokenAuthentication,)
    # user can view status but have to login to post
    # permission_classes = (PostOwnStatus, IsAuthenticatedOrReadOnly)
    # user have to login to view the status also
    permission_classes = (PostOwnStatus, IsAuthenticated)
    serializer_class = ProfileFeedItemSerializer
    queryset = ProfileFeedItem.objects.all()

    def perform_create(self, serializer):
        'sets the user to the logged in user'

        serializer.save(user=self.request.user)
