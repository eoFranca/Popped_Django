from rest_framework.viewsets import ModelViewSet

from core.models import Cliente
from core.serializers import ClienteSerializer


class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
