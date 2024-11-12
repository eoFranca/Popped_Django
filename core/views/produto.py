from django_filters import CharFilter, FilterSet
from rest_framework.viewsets import ModelViewSet

from core.models import Produto
from core.serializers import ProdutoSerializer


class ProdutoFilter(FilterSet):
    categoria = CharFilter(field_name="categoria__descricao", lookup_expr="contains")

    class Meta:
        model = Produto
        fields = ["categoria"]


class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    filterset_class = ProdutoFilter

    # def get_ser
