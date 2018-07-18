from django.urls import path

from . import views

urlpatterns = [
    
    path("", views.home),
    path("menu/", views.menu),
    path('toppings/<int:topping_id>/', views.add_toppings),
	path("toppings/", views.topping_menu, name = 'abc'),
	
    path("register/", views.register),
    path("login/", views.login_page),
    path("logout/", views.logout_page),
    path('cart/<int:product_id>/', views.add_to_cart),
    path('cart/', views.get_cart),
    path('cart_remove/<int:order_id>/', views.remove_order),


]
