from django.shortcuts import render
from shop_app.models import Product


def index(request):
  products = Product.objects.all()
  return render(request, 'index.html', context={ 'products': products })


def product(request, product_id):
  product = Product.objects.get(id=product_id)
  return render(request, 'product.html', context={ 'product': product })


  def customers (request, product_id):
  customers = customers.objects.all(id=customers_id)
  return render(request, 'customers.html', context={ 'customers': customers })