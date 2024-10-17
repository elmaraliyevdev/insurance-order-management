from rest_framework import serializers
from .models import InsuranceProduct, InsuranceOrder


class InsuranceProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsuranceProduct
        fields = ['id', 'name', 'price', 'description', 'status']


class InsuranceOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsuranceOrder
        fields = ['id', 'user', 'product', 'status', 'creation_date', 'closing_date']
        read_only_fields = ['user', 'creation_date', 'closing_date']


class OrderCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsuranceOrder
        fields = ['product']  # Only need product for order creation
