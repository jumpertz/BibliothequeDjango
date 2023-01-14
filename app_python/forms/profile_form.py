from django import forms
from django.contrib.auth.models import User


class ProfilForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ['username']  # ['name', 'language']
        exclude = ()  # ['created_by', ]

class UploadFileForm(forms.Form):
    file = forms.FileField()

