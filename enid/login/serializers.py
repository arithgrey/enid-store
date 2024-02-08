from django.contrib.auth.models import User
from rest_framework import serializers
from user.serializers.user_validator_serializers import CustomEmailValidator
from django.core.validators import  validate_email as django_validate_email

class UserSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    name = serializers.CharField(write_only=True)  # Agrega el campo name

    class Meta:
        model = User
        fields = ['name','email','password']        

    def validate_email(self, value):
        """            
            Validate unique email
        """
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Ya existe un usuario con este email.")
        return value
    
    def create(self, validated_data):
        name = validated_data.pop('name', '')
        validated_data['first_name'] = name
        validated_data['username'] = validated_data['email']

        user = User.objects.create_user(**validated_data)
        return user


class UserSingInValidatorSerializer(serializers.Serializer):
    
    email = serializers.EmailField(        
        required=True,
        allow_blank=False,
        validators=[CustomEmailValidator(), django_validate_email],  
        error_messages={
            'required': 'El campo "email" es obligatorio.',
            'blank': 'El campo "email" no puede estar vacío.',
            'invalid': 'Ups! este email no parece ser correcto'
        })
    
    password = serializers.CharField(                
        required=True,
        allow_blank=False,
        error_messages={
            'required': 'Hey ingresa tu password!',
            'blank': 'Hey ingresa tu password!',
        }
    )
    
    class Meta:
        
        fields = ['email','password']        
        required_fields = ["email", "password"]
        not_allow_blank = ["email", "password"]
        max_lengths = {}
        min_lengths = {}
        min_values = {}
        max_values = {}        
