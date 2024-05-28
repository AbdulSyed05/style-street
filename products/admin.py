from django.contrib import admin
from .models import Product, Category, Condition

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Condition)
