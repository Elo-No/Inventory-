
from django.urls import path, include

urlpatterns = [
    path("", include("apps.product.apis.v1.urls")),
]