from django import forms
from django.contrib.auth.models import User


class UserUpdateForm(forms.ModelForm):
    class Meta():
        model = User
        exclude = ['password', 'username', 'is_staff', 'user_permissions', 'is_active', 'is_superuser', 'date_joined']  # ['created_by', ]
        fields = '__all__'  # ['name', 'language']
