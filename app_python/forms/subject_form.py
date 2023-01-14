from django.forms import ModelForm
from ..models import Subject, User
from django import forms


class SubjectForm(ModelForm):
    class Meta():

        model = Subject
        fields = '__all__'  # ['name', 'language']
        exclude = ()  # ['created_by', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(
            groups__name__in=['professor'])
