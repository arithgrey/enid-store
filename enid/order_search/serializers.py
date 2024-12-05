from rest_framework import serializers
from order.models import Order
from order.serializer_status import BaseOrderSerializer
class OrderSearchSerializer(BaseOrderSerializer):
    visible_statuses_admin = serializers.SerializerMethodField()

    class Meta(BaseOrderSerializer.Meta):
        fields = '__all__'

    def get_visible_statuses_admin(self, obj):
        return [
            {"key": key, "label": label}
            for key, label in Order.STATUS_CHOICES
            if key in Order.ADMIN_TIMELINE_VISIBLE_STATUSES
        ]
