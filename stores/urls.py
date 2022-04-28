from django.urls import path
from .views import (
  InputAddressView, ProductDetailView, ProductListView, add_product, CartItemsVIew, CartUpdateView, CartDeleteView, ConfirmOrderView, OrderSuccessVIew
)

app_name = 'stores'
urlpatterns= [
  path('product_list/', ProductListView.as_view(), name='product_list'),
  path('product_detail/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
  path('add_product/', add_product, name='add_product'),
  path('cart_items/', CartItemsVIew.as_view(), name='cart_items'),
  path('update_cart/<int:pk>', CartUpdateView.as_view(), name='update_cart'),
  path('delete_cart/<int:pk>', CartDeleteView.as_view(), name='delete_cart'),
  path('input_address/', InputAddressView.as_view(), name='input_address'),
  path('input_address/<int:pk>', InputAddressView.as_view(), name='input_address'),
  path('confirm_order/', ConfirmOrderView.as_view(), name='confirm_order'),
  path('order_success/', OrderSuccessVIew.as_view(), name='order_success'),

]
