from rest_framework import serializers

from core.models import Pedido
from core.serializers.produto import ProdutoPedidoSerializer

class PedidoSerializer(serializers.ModelSerializer):
    produto = ProdutoPedidoSerializer(many=True)
    class Meta:
        model = Pedido
        fields = ["id", "produto", "data_criacao"]
        depth = 1

class PedidoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ["id", "produto"]

class TotalSerializer(serializers.Serializer):
    total = serializers.DecimalField(max_digits=10, decimal_places=2)
