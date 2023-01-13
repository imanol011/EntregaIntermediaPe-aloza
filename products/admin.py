from django.contrib import admin

from products.models import Products
# Register your models here.


# admin.site.register(Products)
@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')
    list_filter = ('stock', 'price') #filtrar
    search_fields = ('name',) #buscar