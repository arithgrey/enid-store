from rest_framework import viewsets, status
from rest_framework.response import Response
from lead.models import Lead
from lead_search.serializers import LeadSearchSerializer
from django.db.models import Q
from store.mixin import StoreIDMixin
from rest_framework.decorators import action


class LeadSearchViewSet(StoreIDMixin, viewsets.ViewSet):
        
    def search(self, request):
        
        store = self.get_store_or_default(request)      
        if isinstance(store, Response):
            return store  
               
        leads = self.perform_search(request, store=store)        
        serializer = LeadSearchSerializer(leads, many=True)
        return Response(serializer.data)
    
    
    def perform_search(self,request, store):
        
        q = request.query_params.get('q', None)        
        status = request.query_params.get('status', 'pending')        
        
        if q is None:            

            return Lead.objects.filter(
                status=status, store_id=store).order_by('-created_at')[:30]

        else:   
            
            return Lead.objects.filter(
                Q(name__icontains=q) |        
                Q(email__icontains=q) |            
                Q(phone_number__icontains=q),   
                status=status,
                store_id=store.id
            )
