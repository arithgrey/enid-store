from rest_framework import serializers
from .models import Returns
from django.contrib.auth.models import User

class ReturnsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Returns
        fields = ['id', 'ask', 'short_answer','path_seccion','call_to_action']