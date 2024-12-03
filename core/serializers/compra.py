from rest_framework.serializers import CharField, ModelSerializer, SerializerMethodField

from core.models import Compra, ItensCompra


class ItensCompraSerializer(ModelSerializer):
    total = SerializerMethodField()

    def get_total(self, instance):
        return instance.livro.preco * instance.quantidade

    class Meta:
        model = ItensCompra
        fields = ("produto", "quantidade")
        depth = 1


class CompraSerializer(ModelSerializer):
    class Meta:
        model = Compra
        fields = ("id", "usuario", "status", "total", "itens")
        usuario = CharField(source="usuario.email", read_only=True)
        status = CharField(source="get_status_display", read_only=True)
        itens = ItensCompraSerializer(many=True, read_only=True)


class ItensCompraCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = ("produto", "quantidade")


class CompraCreateUpdateSerializer(ModelSerializer):
    itens = ItensCompraCreateUpdateSerializer(many=True)

    class Meta:
        model = Compra
        fields = ("usuario", "itens")

    def update(self, compra, validated_data):
        itens = validated_data.pop("itens")
        if itens:
            compra.itens.all().delete()
            for item in itens:
                item["preco"] = item["livro"].preco  # nova linha
                ItensCompra.objects.create(compra=compra, **item)
        compra.save()
        return super().update(compra, validated_data)

    def create(self, validated_data):
        itens = validated_data.pop("itens")
        compra = Compra.objects.create(**validated_data)
        for item in itens:
            item["preco"] = item["produto"].preco
            ItensCompra.objects.create(compra=compra, **item)
        compra.save()
        return compra
