from django.shortcuts import render

# Create your views here.
def index(request):
    return render (request,"Home/index.html")
def ListProducts(request):
    """g"""
    return render(request,"ProductList/list_layout.html")
def ProductDetail(request):
    return render(request,"Products/product_page_layout.html")
