from django.shortcuts import render
from .models import Product
# Create your views here.
def index(request):
    
    return render (request,"Home/index.html")
def ListProducts(request):
    obj = Product.objects.all()
    
    return render(request,"ProductList/list_layout.html",{"obj":obj})
def ProductDetail(request,id):
    obj = Product.objects.get(id=id)
    
    return render(request,"Products/product_page_layout.html",{"product":obj})
def ProductByBrands(request,brand):
    print(brand)
    obj = Product.objects.filter(brand=brand)
    return render(request,"ProductList/list_layout.html",{"obj":obj})
