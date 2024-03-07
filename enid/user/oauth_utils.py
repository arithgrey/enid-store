from rest_framework.response import Response
from rest_framework import status

class AuthenticationChecker:
    @staticmethod
    def check_authentication(request):
        if not request.user.is_authenticated:
            return Response({"error": "Usuario no autenticado"}, status=status.HTTP_401_UNAUTHORIZED)
        return None