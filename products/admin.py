from django.contrib import admin
from products.models import Product, Category


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'amount', 'total_price', 'display_categories')
    list_filter = ('price', 'amount', 'categories')
    search_fields = ('title',)
    list_per_page = 10
    ordering = ('price', 'amount')

    def total_price(self, obj):
        return obj.price * obj.amount
    total_price.short_description = 'Total price'

    def display_categories(self, obj):
        return ', '.join([category.title for category in obj.categories.all()])
    display_categories.short_description = 'Categories'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_per_page = 10
    ordering = ('title',)
