from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import InsuranceProduct, InsuranceOrder, CustomUser


class APITests(APITestCase):

    def setUp(self):
        # Create a user and log them in
        self.user = CustomUser.objects.create_user(username="testuser", password="testpassword", role="client")
        self.client.login(username="testuser", password="testpassword")

        # Create some insurance products
        self.product1 = InsuranceProduct.objects.create(
            name="Auto Insurance", price=1000.00, description="Covers vehicle damage", status="active")
        self.product2 = InsuranceProduct.objects.create(
            name="Health Insurance", price=500.00, description="Covers health costs", status="active")

        # URL reverses for endpoints
        self.products_url = reverse('product-list')
        self.orders_url = reverse('order-list')
        self.order_create_url = reverse('order-create')

    # Test fetching active products
    def test_get_active_products(self):
        response = self.client.get(self.products_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # We expect 2 active products
        self.assertEqual(response.data[0]['name'], "Auto Insurance")
        self.assertEqual(response.data[1]['name'], "Health Insurance")

    # Test fetching user orders
    def test_get_user_orders(self):
        # Create an order for the test user
        InsuranceOrder.objects.create(user=self.user, product=self.product1, status='new')

        response = self.client.get(self.orders_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['product'], self.product1.id)
        self.assertEqual(response.data[0]['status'], 'new')

    # Test fetching order status
    def test_get_order_status(self):
        # Create an order
        order = InsuranceOrder.objects.create(user=self.user, product=self.product1, status='new')

        # Reverse the URL to get the status of the order
        order_status_url = reverse('order-status', kwargs={'pk': order.id})

        response = self.client.get(order_status_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'new')

    # Test creating an order without authentication
    def test_create_order_unauthenticated(self):
        self.client.logout()
        data = {
            "product": self.product1.id
        }
        response = self.client.post(self.order_create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
