from rest_framework import serializers


class MonthlyRevenueSerializer(serializers.Serializer):
    month = serializers.IntegerField()
    recibidos = serializers.DecimalField(max_digits=14, decimal_places=2)
    pendientes = serializers.DecimalField(max_digits=14, decimal_places=2)


class SummaryRevenueSerializer(serializers.Serializer):
    recibidos = serializers.DecimalField(max_digits=14, decimal_places=2)
    pendientes = serializers.DecimalField(max_digits=14, decimal_places=2)
    total = serializers.DecimalField(max_digits=14, decimal_places=2)


class ComparisonSerializer(serializers.Serializer):
    month = serializers.IntegerField()
    current = serializers.DecimalField(max_digits=14, decimal_places=2, allow_null=True)
    previous = serializers.DecimalField(max_digits=14, decimal_places=2, allow_null=True)


class ByProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    image = serializers.CharField(allow_null=True)
    amount = serializers.DecimalField(max_digits=14, decimal_places=2)
    pct = serializers.FloatField()
