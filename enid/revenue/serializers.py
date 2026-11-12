from rest_framework import serializers


class MonthlyRevenueSerializer(serializers.Serializer):
    month = serializers.IntegerField()
    recibidos = serializers.DecimalField(max_digits=14, decimal_places=2)
    pendientes = serializers.DecimalField(max_digits=14, decimal_places=2)


class SummaryRevenueSerializer(serializers.Serializer):
    recibidos = serializers.DecimalField(max_digits=14, decimal_places=2)
    pendientes = serializers.DecimalField(max_digits=14, decimal_places=2)
    total = serializers.DecimalField(max_digits=14, decimal_places=2)
