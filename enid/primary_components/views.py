from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import ProductComponent
from .serializers import ProductComponentSerializer

class ProductComponentViewSet(viewsets.ModelViewSet):
    queryset = ProductComponent.objects.all()
    serializer_class = ProductComponentSerializer

    @action(detail=False, methods=['post'])
    def add_component(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    @action(detail=False, methods=['DELETE'])
    def delete_component(self, request):
        kit_id = request.data.get('kit')
        component_id = request.data.get('component')
        
        if not kit_id or not component_id:
            return Response(
                {"error": "Se requieren los parámetros 'kit' y 'component'"},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        try:
            component = self.queryset.filter(
                kit=kit_id,
                component=component_id
            ).first()
            
            if component:
                component.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(
                    {"error": "Componente no encontrado"},
                    status=status.HTTP_404_NOT_FOUND
                )
                
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )