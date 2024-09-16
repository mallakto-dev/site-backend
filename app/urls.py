from django.contrib import admin
from django.urls import path
from rest_framework import routers

from app.goods.views import CategoryViewSet, GoodViewSet

router = routers.SimpleRouter()
router.register(r"categories", CategoryViewSet)
router.register(r"items", GoodViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
]

urlpatterns += router.urls
