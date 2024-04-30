from django.contrib import admin
from products.models import Product, Category


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'amount', 'total_price')
    list_filter = ('price', 'amount')
    search_fields = ('title',)
    list_per_page = 10
    ordering = ('price', 'amount')

    def total_price(self, obj):
        return obj.price * obj.amount
    total_price.short_description = 'Total price'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_per_page = 10
    ordering = ('title',)
