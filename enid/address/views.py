from django.shortcuts import render
from rest_framework import viewsets
from address.models import Address
from address.serializers.address_serializers import AddressSerializer 

class AddressViewSet(viewsets.ModelViewSet):

    queryset = Address.objects.all()
    serializer_class = AddressSerializer
