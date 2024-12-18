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

    
    def perform_search(self,request, user):
        
        q = request.query_params.get('q', None)        
        status = request.query_params.get('status', 'pending')                        

        if q is None:            

            return Order.objects.filter(
                user=user, status=status).order_by('-created_at')[:30]

        else:   
            
            return Order.objects.filter(                            
                Q(shipping_address__phone_number__icontains=q )|                
                Q(id__icontains=q),                   
                user=user, status=status
            )