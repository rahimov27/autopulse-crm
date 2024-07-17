from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("logout/", views.logout_user, name="logout_user"),
    path("register/", views.register_user, name="register_user"),
    path("car/<int:pk>", views.customer_car, name="car"),
    path("delete_car/<int:pk>", views.delete_car, name="delete_car"),
    path("add_car/", views.add_car, name="add_car"),
]
