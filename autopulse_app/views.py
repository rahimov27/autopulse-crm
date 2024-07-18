# views.py
from rest_framework import viewsets, permissions
from .models import Car
from .serializers import CarSerializer
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import AddCarForm, SignUpForm, UpdateCarForm


class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Car.objects.filter(user=user)
        imei = self.request.query_params.get("imei", None)
        if imei is not None:
            queryset = queryset.filter(imei=imei)
        return queryset


def home(request):
    cars = (
        Car.objects.filter(user=request.user) if request.user.is_authenticated else None
    )
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in")
            return redirect("home")
        else:
            messages.error(request, "There was an error logging in. Please try again.")
            return redirect("home")
    return render(request, "home.html", {"cars": cars})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect("home")


def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully registered")
            return redirect("home")
    else:
        form = SignUpForm()
    return render(request, "register.html", {"form": form})


def customer_car(request, pk):
    if request.user.is_authenticated:
        customer_car = get_object_or_404(Car, pk=pk, user=request.user)
        return render(request, "car.html", {"customer_car": customer_car})
    else:
        messages.error(request, "You must be logged in!")
        return redirect("home")


def delete_car(request, pk):
    if request.user.is_authenticated:
        car_to_delete = get_object_or_404(Car, id=pk, user=request.user)
        car_to_delete.delete()
        messages.success(request, "You deleted the car successfully.")
        return redirect("home")
    else:
        messages.error(request, "You must be logged in to do that.")
        return redirect("home")


def add_car(request):
    if request.method == "POST":
        form = AddCarForm(request.POST)
        if form.is_valid():
            car = form.save(commit=False)
            car.user = request.user
            car.save()
            messages.success(request, "Car added successfully.")
            return redirect("home")
        else:
            messages.error(
                request, "There was an error adding the car. Please try again."
            )
    else:
        form = AddCarForm()
    return render(request, "add_car.html", {"form": form})


def dashboard(request):
    cars = (
        Car.objects.filter(user=request.user) if request.user.is_authenticated else None
    )
    return render(request, "dashboard.html", {"cars": cars})


def update_car(request, pk):
    car = get_object_or_404(Car, pk=pk, user=request.user)
    if request.method == "POST":
        form = AddCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            messages.success(request, "Car updated successfully.")
            return redirect("home")
        else:
            messages.error(
                request, "There was an error updating the car. Please try again."
            )
    else:
        form = AddCarForm(instance=car)
    return render(request, "update_car.html", {"form": form, "car": car})
