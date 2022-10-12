from django.urls import path
from.import views

urlpatterns=[
    path('admin_logo',views.admin_logo),
    path('customer_login',views.customer_login),
    path('customer_signup',views.customer_signup),
    path('project_home',views.project_home),
    path('seller_login',views.seller_login),
    path('seller_signup',views.seller_signup),
]