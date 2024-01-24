from rest_framework import serializers
from faqs.models import Faq


class FaqSerializer(serializers.HyperlinkedModelSerializer):    
    class Meta:
        model = Faq
        fields = ['id', 'ask', 'answer', 'is_visible','url_img','we_mean']
        