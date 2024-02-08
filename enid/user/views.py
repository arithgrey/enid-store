from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User

class UserValidatorViewSet(viewsets.ViewSet):
    
    @action(detail=False, methods=['GET'], url_path='exists')
    def user_exists(self, request, email=None):
        exists =False
        if email is None:
            return Response({'error':"email is required!"}, status=status.HTTP_400_BAD_REQUEST)    
        
        try:
            User.objects.get(email=email)            
            exists = True
        
        except User.DoesNotExist:
            exists =False            

        return Response({"exists":exists}, status=status.HTTP_200_OK)


