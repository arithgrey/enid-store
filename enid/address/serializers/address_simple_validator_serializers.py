from rest_framework import serializers

class AddressSimpleValidatorSerializer(serializers.Serializer):    
        
    street = serializers.CharField(        
        max_length=800, 
        min_length=4, 
        required=True, 
        allow_blank=False,
        error_messages={
            'required': 'Hey te falta indica tu calle',
            'blank': 'Hey te falta este dato!',            
            'max_length': 'La longitud máxima permitida para la calle es de 800 caracteres.',
            'min_length': 'La longitud mínima permitida para la calle es de 30 caracteres.'
        }
        )
    
    phone_number = serializers.CharField(        
        min_length=8, 
        max_length=14,
        required=True,         
        error_messages={
            'required': '''Pasanos tu teléfono, solo hablaremos, 
             si lo necesitamos corroborar algo''',
            'blank': 'Hey te falta este dato!',                        
            'max_length': 'Parece que es muy largo este teléfono',
            'min_length': 'Parece que ese muy corto este teléfono!'            
        }
        )
    class Meta:

        required_fields = [
                "street", 
                "phone_number"
            ]
        
        not_allow_blank = ["postal_code", "street","colony","city"]        
        max_lengths = {"street":300,"colony":100,"phone_number": 20}
        min_lengths = {"street":4, "phone_number":8}
        min_values = {}
        max_values = {}