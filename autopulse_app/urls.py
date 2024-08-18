from django.urls import path
from . import views

urlpatterns = [
    # Other paths...
    path("", views.home, name="home"),
    path("logout/", views.logout_user, name="logout_user"),
    path("cars/", views.cars, name="cars"),
    path("customers/", views.customers, name="customers"),
    path("register/", views.register_user, name="register_user"),
    path("car/<int:pk>", views.customer_car, name="car"),
    path("delete_car/<int:pk>", views.delete_car, name="delete_car"),
    path("add_car/", views.add_car, name="add_car"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("update_car/<int:pk>", views.update_car, name="update_car"),
]
