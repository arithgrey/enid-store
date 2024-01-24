from django.shortcuts import render
from rest_framework import viewsets
from .models import Faq
from faqs.serializers import FaqSerializer


# Create your views here.
    
class FaqViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer
