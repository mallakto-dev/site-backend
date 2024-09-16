from rest_framework import viewsets, mixins

from .models import Category, Good
from .serializers import CategorySerializer, GoodSerializer


class CategoryViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class GoodViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):

    queryset = Good.objects.all()
    serializer_class = GoodSerializer
