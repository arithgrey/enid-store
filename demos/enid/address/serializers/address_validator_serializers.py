from rest_framework import serializers
#from user.serializers.user_validator_serializers import UserValidatorSerializer

class AddressValidatorSerializer(serializers.Serializer):    
    
    #user = UserValidatorSerializer(required=True)    
    
    postal_code = serializers.CharField(            
            required=True,
            min_length=4,
            max_length=10,         
            allow_blank=False,
            error_messages={
                'required': 'Ups! no haz indicado tu Codigo postal',
                'invalid':'hey solo se aceptan números!',
                'min_length':'Ups! no haz indicado tu Codigo postal valido',
                'max_length':'Realmente es tan grande tu código postal?',
                'blank':'Hey! falta tu codigo postal!'
            }
        )
    
    street = serializers.CharField(        
        max_length=100, 
        min_length=4, 
        required=True, 
        allow_blank=False,
        error_messages={
            'required': 'Hey te falta indica tu calle',
            'blank': 'Hey te falta este dato!',            
            'max_length': 'La longitud máxima permitida para la calle es de 200 caracteres.',
            'min_length': 'La longitud mínima permitida para la calle es de 30 caracteres.'
        }
    )
    number = serializers.IntegerField(        
        required=True,
        min_value=1, 
        max_value=9999999,             
        error_messages={
            'required': 'Aun no indicas el numero de casa',
            'blank': 'Hey te falta este dato!',            
            'max_value': 'Seguro tu número de casa es tan grande?',
            'min_value': 'hey! indicanos cual es el número de casa',
            'invalid':'Ingresa un número!'
        })

    colony = serializers.CharField(        
        max_length=100, 
        min_length=3, 
        required=True, 
        allow_blank=False,
        error_messages={
            'required': 'Indicanos tu colonia porfa!',
            'blank': 'Hey te falta este dato!',            
            'max_length': 'Es tan grande el nombre de tu colonia?',
            'min_length': 'Falta tu colonia!'
        }
        )
    delegation_or_municipality = serializers.CharField(        
        max_length=100, 
        min_length=3, 
        required=True,         
        error_messages={
            'required': 'Indicanos tu delegación o municipio!',
            'blank': 'Hey te falta este dato!',            
            'max_length': '¿Es tan largo el nombre de tu delegación?',
            'min_length': 'Hey te falta este dato!'
        }
        )
    city = serializers.CharField(
        
        max_length=100,
        min_length=4,
        required=True, 
        allow_blank=False,
        error_messages={
            'required': 'Falta que nos indiques en qué alcaldia te encuentras!',
            'blank': 'Hey te falta este dato!',            
            'max_length': 'Es tan grande el nombre de tu ciudad?',
            'min_length': 'Falta este campo!'
        })
    
    state = serializers.IntegerField(        
        min_value=1, 
        max_value=32,         
        required=True,         
        error_messages={
            'required': 'No seleccionaste algún estado al que perteneces!',            
            'max_value': 'Ese estado no existe',
            'min_value': 'Ese estado no existe',
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
                "postal_code", 
                "street", 
                "number", 
                "colony", 
                "delegation_or_municipality", 
                "city", 
                "state", 
                "phone_number"
            ]
        
        not_allow_blank = ["postal_code", "street","colony","city"]        
        max_lengths = {"postal_code":10,"street":100,"colony":100,"delegation_or_municipality":100,"city":100,"phone_number":14}
        min_lengths = {"postal_code":4,"street":4,"colony":3,"delegation_or_municipality":3,"city":4,"phone_number":8}
        min_values = {"number":1,"state":1}
        max_values = {"number":9999999,"state":33}
        