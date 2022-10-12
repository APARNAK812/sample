from django.shortcuts import render

# Create your views here.


def add_product(request):
    return render(request,'seller/add product.html')

def home(request):
    return render(request,'seller/home.html')

def product_catalogue(request):
    return render(request,'seller/product catalogue.html')    

def profile(request):
    return render(request,'seller/profile.html')

def update_stocks(request):
    return render(request,'seller/update stocks.html')  

def view_order(request):
    return render(request,'seller/view order.html')  

def change_password(request):
    return render(request,'seller/change password.html')        