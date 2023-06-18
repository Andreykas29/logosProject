from django.contrib import admin
from   shop.models import Product
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'price')
    list_display_links = ('title', )


admin.site.register(Product, ProductAdmin)