from django.urls import path

from apps.product.apis.v1.views import CreateProductAPIView, CreateCategoryAPIView, ListProductAPIView

urlpatterns = [

    path("new/", CreateProductAPIView.as_view(), name="create_product_v1"),
    path("lists/", ListProductAPIView.as_view(), name="list_product_v1"),
    path("category/", CreateCategoryAPIView.as_view(), name="create_category_v1"),

]
