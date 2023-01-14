from django.forms import ModelForm
from ..models import Class, User


class ClassForm(ModelForm):

    class Meta():
        model = Class
        fields = '__all__'  # ['name', 'language']
        exclude = ()  # ['created_by', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(
            groups__name__in=['students'])