from django.shortcuts import render

# Create your views here.

def change_password(request):
    return render(request,'customer/change password.html')


def checkout(request):
    return render(request,'customer/checkout.html')

def home(request):
    return render(request,'customer/home.html')    

def myorders(request):
    return render(request,'customer/myorders.html')    

def productdetails(request):
    return render(request,'customer/productdetails.html')

def profile(request):
    return render(request,'customer/profile.html')   

def mycart(request):
    return render(request,'customer/mycart.html')     
