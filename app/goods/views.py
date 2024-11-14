from rest_framework import viewsets, mixins

from .models import Category, Good
from .serializers import CategorySerializer, GoodSerializer


class CategoryViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):

    queryset = Category.objects.all().prefetch_related("items")
    serializer_class = CategorySerializer
    lookup_field = "slug"


class GoodViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):

    queryset = Good.objects.all().prefetch_related("category")
    serializer_class = GoodSerializer
    lookup_field = "slug"
