from rest_framework import permissions

class TodoPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return super().has_object_permission(obj.user.pk == request.user.pk)