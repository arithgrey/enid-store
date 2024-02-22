from rest_framework import viewsets
from lead_type.models import LeadType
from lead_type.serializers import LeadTypeSerializer

class LeadTypeViewSet(viewsets.ModelViewSet):
    
    queryset = LeadType.objects.all()
    serializer_class = LeadTypeSerializer
    
