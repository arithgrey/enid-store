from rest_framework import serializers
from image.models import Image

class ImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Image
        fields=(
            "id",
            "object_id",
            "title",
            "description",
            "image",
            "is_main",
            "content_type",
            "get_image_url"
            )

    def get_image_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.image.url) if obj.image else None
