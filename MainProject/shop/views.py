from django.shortcuts import render, redirect
from shop.models import Product
from shop.forms import ProductCreateForm
# Create your views here.

# відображення продуктів по категоріям
def itemsPage(request):
    instance = Product.objects.all()
    feed_prod = instance.filter(product_kind='fd')
    accessories_prod = instance.filter(product_kind='ac')
    peel_prod = instance.filter(product_kind='ps')
    context = {
        'instance': instance,
        'feed_prod':feed_prod,
        'accessories_prod':accessories_prod,
        'peel_prod':peel_prod
    }

    return render(request, 'items.html', context)

# створення об'єктів
def create_item(request):
    if request.method == 'POST':
        form = ProductCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('shop:main_shop')
    else:
        form = ProductCreateForm()
    return render(request, 'form_add_item.html', {'form':form})

