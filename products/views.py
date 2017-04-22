from django.shortcuts import render
from .models import Product

def all_products(request):
    pagetitle = "Products"
    subtitle = "Take a look into all products"
    products = Product.objects.all()
    return render(request, "products/products.html", {"products": products, "pagetitle": pagetitle, "subtitle": subtitle})

    