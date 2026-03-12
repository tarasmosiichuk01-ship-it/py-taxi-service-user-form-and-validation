import re

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms


from taxi.models import Driver, Car


class DriverCreationForm(UserCreationForm):
    license_number = forms.CharField(max_length=8)

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ("license_number", )

    def clean_license_number(self):
        license_number = self.cleaned_data["license_number"]
        if not re.match(r"^[A-Z]{3}[0-9]{5}$", license_number):
            raise forms.ValidationError(
                "License number must contain 3 uppercase letters and 5 digits"
            )
        return license_number


class DriverLicenseUpdateForm(forms.ModelForm):
    license_number = forms.CharField(max_length=8)

    class Meta:
        model = get_user_model()
        fields = ("license_number", )

    def clean_license_number(self):
        license_number = self.cleaned_data["license_number"]
        if not re.match(r"^[A-Z]{3}[0-9]{5}$", license_number):
            raise forms.ValidationError(
                "License number must contain 3 uppercase letters and 5 digits"
            )
        return license_number


class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = "__all__"
        widgets = {
            "drivers": forms.CheckboxSelectMultiple
        }
