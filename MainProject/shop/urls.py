from django.urls import path
from shop.views import itemsPage, create_item

app_name='shop'
urlpatterns = [
 path('', itemsPage, name='main_shop'),
 path('create/', create_item, name= 'shop_create'),
]