from django.utils.translation import gettext as _
from rest_framework import serializers
from variants.models import Variant


class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = '__all__'