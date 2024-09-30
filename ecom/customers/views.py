from django.shortcuts import render,redirect
from .models import Customer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
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

    
