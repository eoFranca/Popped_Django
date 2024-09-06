from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Sum

from core.models import Pedido
from core.serializers import PedidoSerializer
from core.serializers import TotalSerializer

class PedidoViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['get'], url_path='total')
    def total(self, request, *args, **kwargs):
        total = Pedido.objects.aggregate(total=Sum('valor'))['total'] or 0
        serializer = TotalSerializer({'total': total})
        return Response(serializer.data)