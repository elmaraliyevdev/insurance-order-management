from django.contrib import admin
from .models import InsuranceProduct, InsuranceOrder, CustomUser


@admin.register(InsuranceProduct)
class InsuranceProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'status']
    search_fields = ['name']
    list_filter = ['status']


@admin.register(InsuranceOrder)
class InsuranceOrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'status', 'creation_date', 'closing_date']
    list_filter = ['status', 'creation_date']
    search_fields = ['user__username', 'product__name']


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'role', 'is_active']
    search_fields = ['username', 'email']
    list_filter = ['role', 'is_active']
