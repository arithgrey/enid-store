from rest_framework import serializers

class SearchValidatorSerializer(serializers.Serializer):
        
    q = serializers.CharField(                
        required=True,
        allow_blank=False,
        error_messages={
            'required': 'Hey ingresa el nombre de algun producto!',
            'blank': 'Hey ingresa el nombre de algun producto!',
        }
    )
    
    class Meta:
        
        fields = ['q']        
        