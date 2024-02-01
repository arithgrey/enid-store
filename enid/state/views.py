from django.shortcuts import render
from rest_framework import viewsets
from state.models import State
from state.serializers import StateSerializer 
# Create your views here.
class StateViewSet(viewsets.ModelViewSet):

    queryset = State.objects.all()
    serializer_class = StateSerializer
