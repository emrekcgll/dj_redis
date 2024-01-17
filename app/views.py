from django.shortcuts import get_object_or_404, render
from django.core.cache import cache
from app.models import Product


def home(request):
    cache_key = f"all_data"
    values = cache.get(cache_key)
    if values is None:
        values = Product.objects.all()
        cache.set(cache_key, values)
        print("@@@@@@@@ DATA FROM DB @@@@@@@@")
    else:
        print("@@@@@@@@ DATA FROM CACHE @@@@@@@@")
    return render(request, 'home.html', {'values': values})


def details(request, pk):
    cache_key = f"product_{pk}"
    value = cache.get(cache_key)
    if value is None:
        value = get_object_or_404(Product, pk=pk)
        cache.set(cache_key, value)
        print("@@@@@@@@ DATA FROM DB @@@@@@@@")
    else:
        print("@@@@@@@@ DATA FROM CACHE @@@@@@@@")
    return render(request, 'details.html', {'value': value})