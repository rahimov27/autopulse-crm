from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Car


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Email Address"}
        ),
    )
    first_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "First Name"}
        ),
    )
    last_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Last Name"}
        ),
    )

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["username"].widget.attrs["placeholder"] = "Username"
        self.fields["username"].label = ""
        self.fields["username"].help_text = (
            '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'
        )

        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["placeholder"] = "Password"
        self.fields["password1"].label = ""
        self.fields["password1"].help_text = (
            '<ul class="form-text text-muted small"><li>Your password can’t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can’t be a commonly used password.</li><li>Your password can’t be entirely numeric.</li></ul>'
        )

        self.fields["password2"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["placeholder"] = "Confirm Password"
        self.fields["password2"].label = ""
        self.fields["password2"].help_text = (
            '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'
        )


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
        ]
        widgets = {
            "vin": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "VIN"}
            ),
            "imei": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "IMEI"}
            ),
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Name"}
            ),
            "renter_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Renter Name"}
            ),
            "monthly_limit": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Monthly Limit"}
            ),
            "oil_change": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Oil Change"}
            ),
            "financial": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Financial"}
            ),
            "status": forms.Select(attrs={"class": "form-control"}),
        }
        labels = {
            "vin": "",
            "imei": "",
            "name": "",
            "renter_name": "",
            "monthly_limit": "",
            "oil_change": "",
            "financial": "",
            "status": "",
        }

    def __init__(self, *args, **kwargs):
        super(AddCarForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            field.label = ""
