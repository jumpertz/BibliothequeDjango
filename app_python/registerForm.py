from django import forms
from .middlewares.validators import validate_phone_number

from app_python.models import User


class SignUpForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    phone_number = forms.CharField(max_length=20, validators=[validate_phone_number])

    def clean_password(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "Les mots de passe ne correspondent pas."
            )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already registered.")
        return email
