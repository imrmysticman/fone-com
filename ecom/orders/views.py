from django.shortcuts import render

# Create your views here.
def Cart(request):
    return render(request,"Cart/cart_layout.html")