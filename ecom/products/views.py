from django.shortcuts import render

# Create your views here.
def index(request):
    return render (request,"index.html")
def ListProducts(request):
    """g"""
    return render(request,"list_layout.html")