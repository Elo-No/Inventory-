from rest_framework.serializers import ModelSerializer
from apps.inventory.models import Inventory, StoreRoom
from apps.product.apis.v1.serializers import ProductSerializer


class StoreRoomSerializer(ModelSerializer):
    class Meta:
        model = StoreRoom
        fields = ('id', 'name', 'address', 'seller')
        read_only = ('id',)


class InventorySerializer(ModelSerializer):
    product = ProductSerializer()
    store_room = StoreRoomSerializer()

    class Meta:
        model = Inventory
        fields = ('id', 'product', 'store_room')
        read_only = ('id',)
