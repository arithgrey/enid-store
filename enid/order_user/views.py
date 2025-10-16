from rest_framework import viewsets, status
from rest_framework.response import Response
from order.models import Order
from order_search.serializers import OrderSearchSerializer
from django.db.models import Q

class OrderSearchViewSet(viewsets.ViewSet):
        
    def search(self, request):
        user = request.user       
        orders = self.perform_search(request, user=user)        
        serializer = OrderSearchSerializer(orders, many=True)
        return Response(serializer.data)

    
    def perform_search(self, request, user):
        """
        Busca órdenes con los siguientes filtros:
        - q: búsqueda por teléfono o ID de orden
        - email: filtra por email del usuario
        - status: filtra por estado de la orden (default: pending)
        """
        q = request.query_params.get('q', None)        
        email = request.query_params.get('email', None)
        status = request.query_params.get('status', 'pending')
        
        # Construir query base con status
        query_filters = Q(status=status)
        
        # Agregar filtro por email si se proporciona
        if email:
            query_filters &= Q(user__email__iexact=email)
        else:
            # Si no hay email en los parámetros, filtrar por usuario autenticado
            query_filters &= Q(user=user)
        
        # Construir consulta
        if q is None:
            # Sin búsqueda de texto, solo filtros
            return Order.objects.filter(query_filters).order_by('-created_at')[:30]
        else:
            # Con búsqueda de texto (teléfono o ID)
            search_filters = (
                Q(shipping_address__phone_number__icontains=q) |                
                Q(id__icontains=q)
            )
            return Order.objects.filter(
                query_filters & search_filters
            ).order_by('-created_at')[:30]