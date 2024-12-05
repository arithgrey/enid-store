from rest_framework import viewsets, status
from rest_framework.response import Response
from order.models import Order
from order_search.serializers import OrderSearchSerializer
from django.db.models import Q

class OrderSearchViewSet(viewsets.ViewSet):
        
    def search(self, request):
        orders = self.perform_search(request)        
        serializer = OrderSearchSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def perform_search(self, request):
        q = request.query_params.get('q', None)        
        status_param = request.query_params.get('status', '').strip()  # Obtener 'status' y eliminar espacios
        
        filter_criteria = Q()
        
        if status_param:
            filter_criteria &= Q(status=status_param)
        
        if q:
            filter_criteria &= (
                Q(shipping_address__phone_number__icontains=q) |
                Q(user__username__icontains=q) |        
                Q(id__icontains=q)
            )
        
        orders = Order.objects.filter(filter_criteria).order_by('-created_at')[:30]
        return orders
