from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

class UserSimpleValidatorSerializer(serializers.Serializer):          
     
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
        required_fields = ["name"]
        not_allow_blank = ["name"]
        max_lengths = {"name":200}
        min_lengths = {"name":3}
        min_values = {}
        max_values = {}
        