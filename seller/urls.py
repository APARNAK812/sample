from django.urls import path
from.import views

urlpatterns=[
    path('add_product',views.add_product),
    path('home',views.home),
    path('product_catalogue',views.product_catalogue),
    path('profile',views.profile),
    path('update_stocks',views.update_stocks),
    path('view_order',views.view_order),
    path('change_password',views.change_password),
]