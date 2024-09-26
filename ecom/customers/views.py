from django.shortcuts import render

# Create your views here.
def Account(request):
    return render(request,"Account/account_layout.html")