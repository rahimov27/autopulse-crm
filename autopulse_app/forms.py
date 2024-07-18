# forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Car


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text="Required")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class AddCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            "vin",
            "imei",
            "name",
            "renter_name",
            "monthly_limit",
            "oil_change",
            "financial",
            "status",
            "final_odometer",
            "car_image",
        ]


class UpdateCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            "vin",
            "imei",
            "name",
            "renter_name",
            "monthly_limit",
            "oil_change",
            "financial",
            "status",
            "final_odometer",
            "car_image",
        ]
