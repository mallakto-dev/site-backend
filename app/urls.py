from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import routers

from app.goods.views import CategoryViewSet, GoodViewSet
from app.orders.views import OrderViewSet
from app.settings import DEBUG


router = routers.SimpleRouter()
router.register(r"categories", CategoryViewSet)
router.register(r"items", GoodViewSet)
router.register(r"order", OrderViewSet)

admin.site.site_header = "Админ-панель Mallakto"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="docs"
    ),
]
if DEBUG:
    urlpatterns += path("__debug__/", include("debug_toolbar.urls"))

urlpatterns += router.urls
