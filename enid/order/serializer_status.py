from rest_framework import serializers
from order.models import Order
from item_order.serializer import ItemOrderSerializer


class BaseOrderSerializer(serializers.ModelSerializer):
    items = ItemOrderSerializer(many=True, read_only=True)
    status_choices = serializers.SerializerMethodField()
    visible_statuses = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = '__all__'

    def get_status_choices(self, obj):
        return [
            {"key": key, "label": label}
            for key, label in Order.STATUS_CHOICES
        ]

    def get_visible_statuses(self, obj):
        return [
            {"key": key, "label": label}
            for key, label in Order.STATUS_CHOICES
            if key in Order.CLIENT_VISIBLE_STATUSES
        ]
