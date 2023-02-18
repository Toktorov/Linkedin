from rest_framework import permissions

class ChatPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(obj.from_user.pk == request.user.pk or obj.to_user.pk == request.user.pk)