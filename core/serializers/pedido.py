from rest_framework import serializers

from core.models import Pedido


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ["id", "valor", "data_criacao"]


class TotalSerializer(serializers.Serializer):
    total = serializers.DecimalField(max_digits=10, decimal_places=2)
