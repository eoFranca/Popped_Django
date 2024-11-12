from rest_framework.serializers import ModelSerializer, SlugRelatedField

from core.models import Cliente
from uploader.models import Image
from uploader.serializers import ImageSerializer


class ClienteSerializer(ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"
        capa_attachment_key = SlugRelatedField(
            source="capa",
            queryset=Image.objects.all(),
            slug_field="attachment_key",
            required=False,
            write_only=True,
        )
        capa = ImageSerializer(required=False, read_only=True)


class ClienteDetailSerializer(ModelSerializer):
    capa = ImageSerializer(required=False)
