from rest_framework import permissions


class UpdateOwnprofile(permissions.BasePermission):
    '''Allow users edit their own profile '''

    def has_object_permission(self, request, view, obj):
        '''Check user is trying to edit their own profile.'''
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class PostOwnStatus(permissions.BasePermission):
    '''Allow user to update their own statue'''

    def has_object_permission(self, request, view, obj):
        '''Checks the user is trying to update their own staus'''
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user.id == request.user.id
