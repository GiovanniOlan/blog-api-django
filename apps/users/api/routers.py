from apps.users.api.views import *
from django.urls import path

app_label = "users"

urlpatterns = [
    path("auth/register/", RegisterView.as_view(), name="register"),
]
