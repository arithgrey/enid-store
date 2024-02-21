from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from login.serializers import UserSignupSerializer, UserSingInValidatorSerializer
from rest_framework.exceptions import ValidationError
from user.serializers.user_validator_serializers import UserValidatorSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import Group
from rest_framework.permissions import IsAuthenticated


class LoginViewSet(viewsets.ViewSet):
    @api_view(['POST'])
    def signup(request):
        data = request.data
        try:

            errors = LoginViewSet.validator_handler(data=data)
            if errors:
                return Response(errors, status=status.HTTP_400_BAD_REQUEST)    

            serializer = UserSignupSerializer(data=data)
            if serializer.is_valid():
                user = serializer.save()
                perfil = Group.objects.get(name='ecommerce')
                user.groups.add(perfil)

                return  Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        except ValidationError as error:
            
            return Response({"detail": error.detail}, status=status.HTTP_400_BAD_REQUEST)


    @staticmethod
    def validator_handler(data):
        errors = {}
        user_serializer = UserValidatorSerializer(data=data)
        if not user_serializer.is_valid():
            errors.update(user_serializer.errors)

        return errors


class LoginSiginViewSet(viewsets.ViewSet):
    
    @api_view(['POST'])
    def sigin(request):        
        data = request.data

        serializer = UserSingInValidatorSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        email = request.data.get('email')
        password = request.data.get('password')
        
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            
            access_token = AccessToken.for_user(user)       
            refresh_token = RefreshToken.for_user(user)                
            profile = user.groups.first().name if user.groups.exists() else None
            user_data = {
               'profile':profile,
               'name': user.first_name,
               'email':user.email,               
            }
            return Response(
                {   'user':user_data,
                    'token': str(access_token), 
                    'refresh_token': str(refresh_token),
                    'profile':profile}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)



class TokenViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    
    @api_view(['POST'])
    def refresh_token(request):       
        try:
            refresh_token = request.data.get('refresh_token')
            if not refresh_token:
                return Response({'error': 'Refresh token is required'}, status=400)

            token = RefreshToken(refresh_token)
            new_access_token = str(token.access_token)
            new_refresh_token = str(token)
                        
            return Response({'access_token': new_access_token, 'refresh_token': new_refresh_token}, status=200)

        except Exception as e:
            return Response({'error': str(e)}, status=500)