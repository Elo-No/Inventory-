from django.urls import path

from apps.inventory.apis.v1.views import CreateStorRoomAPIView

urlpatterns = [
    path("store-room/", CreateStorRoomAPIView.as_view(), name="create_store-room_v1"),
]
