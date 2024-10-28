from rest_framework.routers import DefaultRouter

from apps.categories.api.views import CategoryViewSet

router_categories = DefaultRouter()
router_categories.register(
    prefix="categories", basename="categories", viewset=CategoryViewSet
)
