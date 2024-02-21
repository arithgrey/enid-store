from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):        
        try:
            refresh_token = request.data.get('refresh_token')

            if refresh_token:                
                RefreshToken(refresh_token).blacklist()
                
                return Response({'message': 'Logout exitoso'}, status=status.HTTP_205_RESET_CONTENT)
            else:
                return Response({'error': 'Se requiere un token de refresco'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
