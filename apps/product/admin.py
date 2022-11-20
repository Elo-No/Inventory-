from django.contrib import admin

# Register your models here.
from apps.core.admin import AbstractBaseAdmin
from apps.product.models.category import Category
from apps.product.models.product import Product


@admin.register(Category)
class CategoryAdmin(AbstractBaseAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(Product)
class ProductAdmin(AbstractBaseAdmin):
    list_display = ('name', 'category_name')

    def category_name(self, obj):
        return obj.catergory.name

    category_name.short_description = 'category'
