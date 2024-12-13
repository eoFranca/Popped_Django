from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.models import Compra
from core.serializers import CompraCreateUpdateSerializer, CompraSerializer


class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer

    def get_serializer_class(self):
        if self.action in ("create", "update"):
            return CompraCreateUpdateSerializer
        return CompraSerializer
