from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_url', 'description', 'type', 'brand', 'price', 'available')
    search_fields = ('name', 'type', 'brand')

admin.site.register(Product, ProductAdmin)
