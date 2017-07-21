# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework.viewsets import ViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

from .serializers import HelloSerializer


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
