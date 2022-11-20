from rest_framework.generics import CreateAPIView

from apps.core.permissions import IsAdminOrReadOnly
from apps.inventory.apis.v1.serializers import StoreRoomSerializer


class CreateStorRoomAPIView(CreateAPIView):
    serializer_class = StoreRoomSerializer
    permission_classes = [IsAdminOrReadOnly]
