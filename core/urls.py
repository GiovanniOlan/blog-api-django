from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from apps.categories.api.routers import router_categories

schema_view = get_schema_view(
    openapi.Info(
        title="Blog API",
        default_version="v1",
        description="Documentación de la API del Blog",
        terms_of_service="",
        contact=openapi.Contact(email="gioolanperez@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    # permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # drf_yasg(documentation)
    path(
        "docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redocs/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("api/", include("apps.users.api.routers")),
    # myapps
    path("admin/", admin.site.urls),
    path("api/", include(router_categories.urls)),
]
