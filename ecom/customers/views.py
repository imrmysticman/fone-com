from queue import Full
from django.shortcuts import get_object_or_404, render,redirect
from .models import Customer
from orders.models import Order,OrderItem
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import AddressForm
# Create your views here.
def Account(request):
    context={}
    if request.POST and "register" in request.POST:
        context["register"] = True
        try:
            username= request.POST.get("username")
            email=request.POST.get("email")
            phone = request.POST.get("phone")
            password= request.POST.get("password")
            user = User.objects.create_user(username=username,
                                        email=email,
                                        password=password)
            user.save()
            customer = Customer.objects.create(name=username,user=user,phone=phone)
            customer.save()
            message="successfully registered"  
            messages.success(request,message)          
        except Exception as e:
            error_message = "Duplicate User or Invalid Credentials"
            messages.error(request,error_message)
        return render(request,"Account/account_layout.html",context)

    elif request.POST and "login" in request.POST:
        context["register"] = False

        try:
            print(request.POST)
            username= request.POST.get("username")
            password= request.POST.get("password")
            print (username,password)
            user = authenticate(request,username=username,password=password)
            print(user)
            if user:
                login(request,user)
                return redirect("index")
            success_message="login successful"
            message.success(request,success_message)
            print("success")
            return render(request,"Account/account_layout.html",context)

        except Exception as e:
            error_message = "Invalid Credentials"
            messages.error(request,error_message)
            return render(request,"Account/account_layout.html",context)

        

    else:
        return render(request,"Account/account_layout.html")
def Logout(request):
    logout(request)
    return render(request,"Account/account_layout.html")

def Profile(request):
    if request.user:        
        user = request.user
        customer=user.customer
        print(customer)
        orders=Order.objects.filter(owner=customer).order_by('-created_at')
        obj=[]
        for items in orders:
            order = items.cart.all()
            print(items.order_status)
            print(order)
            obj.append({"status":items.order_status,"orders":order,"date":items.created_at,"id":items.id})
        print(obj)
        return render(request,"Account/Profile_layout.html",{"obj":obj,"customer":customer,"email" : user.email})
    else:
        return redirect("login")

def Address(request):

    if request.user.is_authenticated:
        customer = request.user.customer

        if request.method=="POST":
            form = AddressForm(request.POST)
            if form.is_valid():
                address=form.save()
                address.sav,e()
                customer.address = address
                customer.save()
                return redirect("profile")
        user = request.user
        if customer.address:
            form = AddressForm(instance=customer.address)


        return render(request,"Account/edit_address_layout.html",{"form":form,"customer":customer,"email":request.user.email,})



    
