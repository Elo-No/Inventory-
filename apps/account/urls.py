from django.urls import path, include

urlpatterns = [
    path("", include("apps.account.apis.v1.urls")),
]