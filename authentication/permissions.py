from rest_framework import permissions


class IsAccountOwner(permissions.BasePermissions):
    def has_object_permission(self, request, view, account):
        if request.user:
            return account == request.user
        return False
