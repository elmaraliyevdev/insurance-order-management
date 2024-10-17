from django.urls import path
from .views import ProductListView, OrderListView, OrderCreateView, OrderStatusView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('order/create/', OrderCreateView.as_view(), name='order-create'),
    path('order/<int:pk>/status/', OrderStatusView.as_view(), name='order-status'),
]