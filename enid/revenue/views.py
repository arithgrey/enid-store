from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from django.db.models import Sum, F, DecimalField
from django.db.models.functions import ExtractMonth
from django.utils import timezone
from item_order.models import ItemOrder
from products.models import Product
from revenue.serializers import (
    MonthlyRevenueSerializer, SummaryRevenueSerializer,
    ComparisonSerializer, ByProductSerializer,
)
from decimal import Decimal
from revenue.constants import RECIBIDOS, PENDIENTES, ALL_COUNTED


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


def _year_total_by_month(year, statuses):
    """Returns {month: total} for a given year and status list."""
    qs = (
        ItemOrder.objects
        .filter(order__created_at__year=year, order__status__in=statuses)
        .annotate(month=ExtractMonth('order__created_at'))
        .values('month')
        .annotate(total=Sum(F('price') * F('quantity'), output_field=DecimalField()))
    )
    return {r['month']: r['total'] for r in qs}


class ComparisonRevenueView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        now = timezone.now()
        year = int(request.query_params.get('year', now.year))
        current_map = _year_total_by_month(year, ALL_COUNTED)
        previous_map = _year_total_by_month(year - 1, ALL_COUNTED)
        # For the current calendar year, future months return null; for past years, show 0.
        current_month = now.month if year == now.year else 12

        data = []
        for m in range(1, 13):
            if m <= current_month:
                current_val = current_map.get(m, Decimal('0.00'))
            else:
                current_val = None
            previous_val = previous_map.get(m, Decimal('0.00'))
            data.append({'month': m, 'current': current_val, 'previous': previous_val})
        return Response(ComparisonSerializer(data, many=True).data)


class ByProductRevenueView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        now = timezone.now()
        year = int(request.query_params.get('year', now.year))
        month = int(request.query_params.get('month', now.month))

        rows = list(
            ItemOrder.objects
            .filter(
                order__created_at__year=year,
                order__created_at__month=month,
                order__status__in=ALL_COUNTED,
            )
            .values('product_id')
            .annotate(amount=Sum(F('price') * F('quantity'), output_field=DecimalField()))
            .order_by('-amount')
        )

        if not rows:
            return Response([])

        total = sum(r['amount'] for r in rows) or Decimal('1')
        product_ids = [r['product_id'] for r in rows]
        products = {p.id: p for p in Product.objects.filter(id__in=product_ids)}

        data = []
        for r in rows:
            p = products.get(r['product_id'])
            image_url = None
            if p:
                first_image = p.images.first()
                if first_image and first_image.image:
                    try:
                        image_url = str(first_image.image.url)
                    except Exception:
                        image_url = None
            data.append({
                'id': r['product_id'],
                'name': p.name if p else '',
                'image': image_url,
                'amount': r['amount'],
                'pct': round(float(r['amount'] / total * 100), 1),
            })
        return Response(ByProductSerializer(data, many=True).data)
