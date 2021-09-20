from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """ Alow Users to edit their own profile"""

    def has_object_permission(self,request,view,obj):
        """ Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        # Check  if the request user id i.e. the person logged in is same as the obj which has to be updated
        return obj.id == request.user.id
