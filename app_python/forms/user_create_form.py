from django import forms
from django.contrib.auth.models import User


class UserCreateForm(forms.ModelForm):
    class Meta():
        model = User
        widgets = {
            'password': forms.PasswordInput()
        }
        exclude = ['username', 'is_staff', 'user_permissions', 'is_active', 'is_superuser', 'date_joined']  # ['created_by', ]
        fields = '__all__'  # ['name', 'language']

    def clean(self):
        super().clean()
        self.instance.username = self.cleaned_data.get('first_name', 0)[0] + self.cleaned_data.get('last_name', 0)
        return self.cleaned_data