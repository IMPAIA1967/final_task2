from rest_framework import permissions


class OwnerOnly(permissions.BasePermission):
    """Только владелец может редактировать"""

    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return obj == request.user or request.user.is_staff


class AuthorOnly(permissions.BasePermission):
    """Только автор может редактировать"""

    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return obj.author == request.user or request.user.is_staff
