from rest_framework.permissions import BasePermission, SAFE_METHODS

"""
CUSTOM PERMISSIONS FOR ACCESSING CERTAIN METHODS (POST, PUT, DELETE etc.)
"""


class IsAdminOrReadOnly(BasePermission):
    """Allows access only is_superuser users"""

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return request.user and request.user.is_superuser


class IsAdminOrReadAndCreateOnly(BasePermission):
    """Only superuser can delete or modify"""

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if request.method == "POST":
            return True

        return request.user and request.user.is_superuser
