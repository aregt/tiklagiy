from django.shortcuts import render
from products.models import Product
from stores.models import Store

def home(request):
    latest_products = Product.objects.order_by('-created_at')[:5]  # Son 5 ürün
    featured_stores = Store.objects.order_by('?')[:3]  # Rastgele 3 mağaza
    context = {
        'latest_products': latest_products,
        'featured_stores': featured_stores,
    }
    return render(request, 'home.html', context)