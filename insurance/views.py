from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import InsuranceProduct, InsuranceOrder
from .serializers import InsuranceProductSerializer, InsuranceOrderSerializer, OrderCreationSerializer


# Fetch Active Products
class ProductListView(generics.ListAPIView):
    queryset = InsuranceProduct.objects.filter(status='active')
    serializer_class = InsuranceProductSerializer
    permission_classes = [permissions.AllowAny]


# Fetch All Orders for the Current User
class OrderListView(generics.ListAPIView):
    serializer_class = InsuranceOrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return InsuranceOrder.objects.filter(user=self.request.user)


# Create a New Insurance Order
class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderCreationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# Get the Status of an Order
class OrderStatusView(generics.RetrieveAPIView):
    queryset = InsuranceOrder.objects.all()
    serializer_class = InsuranceOrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return InsuranceOrder.objects.filter(user=self.request.user)
