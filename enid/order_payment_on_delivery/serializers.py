from rest_framework import serializers

class SourceValidatorSerializer(serializers.Serializer):
    source = serializers.CharField(
        max_length=200,
        required=False,
        allow_blank=True,
        help_text="Identificador de la landing page o fuente de origen",
        error_messages={
            'max_length': 'El campo source no puede exceder 200 caracteres.',
        }
    )
    
    class Meta:
        fields = ['source']
        max_lengths = {"source": 200} 