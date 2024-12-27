from rest_framework.serializers import (
    CharField,
    ModelSerializer,
    SerializerMethodField,
    SlugRelatedField,
)

from core.models import Compra, ItensCompra
from uploader.models import Image
from uploader.serializers import CompraImageSerializer, ImageSerializer


class ItensCompraSerializer(ModelSerializer):
    total = SerializerMethodField()

    def get_total(self, instance):
        return instance.produto.valor * instance.quantidade

    class Meta:
        model = ItensCompra
        fields = ("produto", "quantidade", "total")
        depth = 1


class CompraSerializer(ModelSerializer):
    status = CharField(source="get_status_display", read_only=True)
    itens = ItensCompraSerializer(many=True, read_only=True)
    capa_attachment_key = SlugRelatedField(
        source="capa",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    capa = CompraImageSerializer(required=False, read_only=True)

    class Meta:
        model = Compra
        fields = ("id", "usuario", "status", "total", "itens", "capa", "capa_attachment_key")


class ItensCompraCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = ("produto", "quantidade")


class CompraDetailSerializer(ModelSerializer):
    capa = ImageSerializer(required=False)


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
                item["preco"] = item["produto"].preco
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
