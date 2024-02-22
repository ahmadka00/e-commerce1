from rest_framework import permissions

class IsAdminOrReadOnly(permissions.IsAdminUser):

    def has_permission(self, request, view):
        is_staff = super(IsAdminOrReadOnly, self).has_permission(request, view)
        return request.method in permissions.SAFE_METHODS or is_staff