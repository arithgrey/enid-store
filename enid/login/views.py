from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from login.serializers import UserSignupSerializer, UserSingInValidatorSerializer
from rest_framework.exceptions import ValidationError
from user.serializers.user_validator_serializers import UserValidatorSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password


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
                serializer.save()
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
            refresh = RefreshToken.for_user(user)
            return Response(
                {'token': str(refresh.access_token)}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)