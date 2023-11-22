from rest_framework import serializers
from faqs.models import Faq
from django.contrib.auth.models import User


class FaqSerializer(serializers.HyperlinkedModelSerializer):    
    class Meta:
        model = Faq
        fields = ['id', 'ask', 'answer', 'is_visible']
        