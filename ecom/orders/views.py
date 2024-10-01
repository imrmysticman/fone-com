from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import Order,OrderItem
from products.models import Product
# Create your views here.
def Cart(request):
    if request.user:
        user = request.user
        print(user)
        customer=user.customer
        cart_obj,create=Order.objects.get_or_create(owner=customer,
                                             order_status=Order.CART_STAGE)
        context={"cart":cart_obj}

        return render(request,"Cart/cart_layout.html",context)



    return render(request,"Cart/cart_layout.html")
def AddToCart(request):
    if request.POST:
        user=request.user
        customer = user.customer
        product_id = request.POST.get("product_id")
        quantity = int(request.POST.get("quantity"))
        cart_obj,create=Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE
        )
        cart_obj.save()
        print(cart_obj)
        ordered_item = OrderItem.objects.create(
        product=Product.objects.get(id=product_id),
        quantity=quantity,
        order=cart_obj
        )
        print(ordered_item)
        ordered_item.save()
        return redirect("cart")
        