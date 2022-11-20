from rest_framework.permissions import BasePermission, SAFE_METHODS

from apps.account.enums import UserRole


class IsSellerOrAdminOrReadOnly(BasePermission):
    message = 'Permission denied: just admin and seller can access to  this end point.'

    def has_permission(self, request, view=None):
        try:
            if request.method in SAFE_METHODS:
                return True
            if request.user.is_authenticated() and request.user.role in (UserRole.ADMIN, UserRole.SELLER):
                return True
            return False
        except Exception as e:
            return False

    def has_object_permission(self, request, view, obj):
        try:
            if request.user.is_authenticated() and request.user.role in (UserRole.ADMIN, UserRole.SELLER):
                return True
            return False
        except Exception as e:
            return False


class IsAdminOrReadOnly(BasePermission):
    message = 'Permission denied: just admin  can access to  this end point.'

    def has_permission(self, request, view=None):
        try:
            if request.method in SAFE_METHODS:
                return True
            if request.user.is_authenticated() and request.user.role == UserRole.ADMIN:
                return True
            return False
        except Exception as e:
            return False

    def has_object_permission(self, request, view, obj):
        try:
            if request.method in SAFE_METHODS:
                return True
            if request.user.is_authenticated() and request.user.role == UserRole.ADMIN:
                return True
            return False
        except Exception as e:
            return False
