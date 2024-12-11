from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from core.views import (
    CategoriaViewSet,
    ClienteViewSet,
    CompraViewSet,
    PedidoViewSet,
    ProdutoViewSet,
    UserViewSet,
)


from uploader.router import router as uploader_router

router = DefaultRouter()

router.register(r"pedidos", PedidoViewSet, basename="pedidos")
router.register(r"usuarios", UserViewSet, basename="usuarios")
router.register(r"categorias", CategoriaViewSet, basename="categorias")
router.register(r"produtos", ProdutoViewSet, basename="produtos")
router.register(r"clientes", ClienteViewSet, basename="clientes")
router.register(r"compras", CompraViewSet, basename="compras")
router.registry.extend(uploader_router.registry)

urlpatterns = [
    path("admin/", admin.site.urls),
    # OpenAPI 3
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    # Simple JWT
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # API
    path("api/", include(router.urls)),
]
urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
