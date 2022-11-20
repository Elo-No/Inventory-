from django.contrib import admin

# Register your models here.
from apps.core.admin import AbstractBaseAdmin
from apps.inventory.models import StoreRoom
from apps.inventory.models import Inventory


@admin.register(Inventory)
class InventoryAdmin(AbstractBaseAdmin):
    list_display = ('product_detail', 'quantity','store_room_detail')

    def product_detail(self, obj):
        return obj.product.name

    product_detail.short_description = 'product'

    def store_room_detail(self, obj):
        return obj.store_room.name

    store_room_detail.short_description = 'sore_room'


@admin.register(StoreRoom)
class StoreRoomAdmin(AbstractBaseAdmin):
    list_display = ('name',)
    filter_horizontal = ('seller',)
