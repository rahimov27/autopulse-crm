from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import AddCarForm, SignUpForm
from .models import Car


def home(request):
    if request.user.is_authenticated:
        cars = Car.objects.filter(user=request.user)
    else:
        cars = None

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
        car_to_delete = get_object_or_404(Car, pk=pk, user=request.user)
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
