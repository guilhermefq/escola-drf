from rest_framework import permissions


# Manualmente definindo as permissões para a viewset
class EhSuperUser(permissions.BasePermission):
    """Se o método for DELETE é o usuário é superuser, permite executar o delete"""

    def has_permission(self, request, view):
        if request.method == 'DELETE':
            if request.user.is_superuser:
                return True
            return False
        return True
