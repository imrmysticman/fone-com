from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import Order,OrderItem
from products.models import Product
# Create your views here.
def Cart(request):
    if request.user:
        user = request.user
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
        cart_obj,created=Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE
        )
        cart_obj.save()
        ordered_item,created = OrderItem.objects.get_or_create(
        product=Product.objects.get(id=product_id),
        order=cart_obj
        )
        if created:
            ordered_item.quantity=quantity
        else:
            ordered_item.quantity=ordered_item.quantity+quantity
        ordered_item.save()
        return redirect("cart")
def removeProduct(request):
    if request.POST:
        obj=request.POST.get("obj_id")
        orderItem=OrderItem.objects.get(id=obj)
        orderItem.delete()
    return redirect("cart")
def checkout(request):
    user=request.user
    customer=user.customer
    order=Order.objects.get(owner=customer,order_status=Order.CART_STAGE)
    if order:
        order.order_status=Order.ORDER_CONFIRMED
        order.save()
        print(order)
    return redirect("cart")
def cancelOrder(request,id):
    item = Order.objects.get(id=id)
    print(item)
    item.order_status=4
    item.save()
    return redirect("profile")

