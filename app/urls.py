from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

from app.goods.views import CategoryViewSet, GoodViewSet
from app.orders.views import OrderViewSet

router = routers.SimpleRouter()
router.register(r"categories", CategoryViewSet)
router.register(r"items", GoodViewSet)
router.register(r"order", OrderViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
]

urlpatterns += router.urls
