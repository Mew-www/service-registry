from rest_framework import permissions


class IsThisUserOrAdministrator(permissions.BasePermission):
    # Object-permission where object is THE user themselves, or AN admin
    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.is_staff


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
