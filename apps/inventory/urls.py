from django.urls import path, include

urlpatterns = [
    path("", include('apps.inventory.apis.v1.urls')),
]
