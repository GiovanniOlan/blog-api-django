from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from apps.categories.api.serializers import CategorySerializer
from apps.categories.models import Category
from apps.categories.api.permissions import IsAdminOrReadOnly


class CategoryViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, IsAdminOrReadOnly)
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
