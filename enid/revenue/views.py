from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from django.db.models import Sum, F, DecimalField
from django.db.models.functions import ExtractMonth
from django.utils import timezone
from item_order.models import ItemOrder
from revenue.serializers import MonthlyRevenueSerializer, SummaryRevenueSerializer
from decimal import Decimal

RECIBIDOS = ['payment_confirmed', 'delivered', 'cash_on_delivery']
PENDIENTES = ['pending', 'preparing', 'ready_for_shipping', 'in_transit', 'ready_for_pickup']


def _monthly_sums(year, group):
    return (
        ItemOrder.objects
        .filter(order__created_at__year=year, order__status__in=group)
        .annotate(month=ExtractMonth('order__created_at'))
        .values('month')
        .annotate(total=Sum(F('price') * F('quantity'), output_field=DecimalField()))
    )


class MonthlyRevenueView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        year = int(request.query_params.get('year', timezone.now().year))
        recibidos_qs = _monthly_sums(year, RECIBIDOS)
        pendientes_qs = _monthly_sums(year, PENDIENTES)

        recibidos_map = {r['month']: r['total'] for r in recibidos_qs}
        pendientes_map = {r['month']: r['total'] for r in pendientes_qs}

        data = [
            {
                'month': m,
                'recibidos': recibidos_map.get(m, Decimal('0.00')),
                'pendientes': pendientes_map.get(m, Decimal('0.00')),
            }
            for m in range(1, 13)
        ]
        return Response(MonthlyRevenueSerializer(data, many=True).data)


class SummaryRevenueView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        now = timezone.now()
        year = int(request.query_params.get('year', now.year))
        month = int(request.query_params.get('month', now.month))

        def _sum(statuses):
            result = (
                ItemOrder.objects
                .filter(
                    order__created_at__year=year,
                    order__created_at__month=month,
                    order__status__in=statuses,
                )
                .aggregate(total=Sum(F('price') * F('quantity'), output_field=DecimalField()))
            )
            return result['total'] or Decimal('0.00')

        recibidos = _sum(RECIBIDOS)
        pendientes = _sum(PENDIENTES)
        data = {
            'recibidos': recibidos,
            'pendientes': pendientes,
            'total': recibidos + pendientes,
        }
        return Response(SummaryRevenueSerializer(data).data)
