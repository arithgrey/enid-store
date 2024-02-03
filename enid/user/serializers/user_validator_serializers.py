from rest_framework import serializers
from django.core.validators import EmailValidator, validate_email as django_validate_email
from django.utils.translation import gettext_lazy as _


class CustomEmailValidator(EmailValidator):
    message = _('Ups! este email no parece ser correcto')


class UserValidatorSerializer(serializers.Serializer):          
        
    email = serializers.EmailField(        
        required=True,
        allow_blank=False,
        validators=[CustomEmailValidator(), django_validate_email],  
        error_messages={
            'required': 'El campo "email" es obligatorio.',
            'blank': 'El campo "email" no puede estar vacío.',
            'invalid': 'Ups! este email no parece ser correcto'
        })
    
    name = serializers.CharField(        
        max_length=200,
        min_length=3,
        required=True,
        allow_blank=False,
        error_messages={
            'required': 'El campo "name" es obligatorio.',
            'blank': 'El campo "name" no puede estar vacío.',
            'max_length':'Ese nombre es muy grande!'
            
        }
    )
    class Meta:

        fields = '__all__' 
        required_fields = ["email", "name"]
        not_allow_blank = ["email", "name"]
        max_lengths = {"name":200}
        min_lengths = {"name":3}
        min_values = {}
        max_values = {}
        