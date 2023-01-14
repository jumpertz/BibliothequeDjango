from django.forms import ModelForm
from ..models import Note, Subject, User


class NoteForm(ModelForm):

    class Meta():
        model = Note
        fields = '__all__'  # ['name', 'language']
        exclude = ()  # ['created_by', ]

    def __init__(self, *args, **kwargs):
        user_id = kwargs.pop('user_id')
        super().__init__(*args, **kwargs)
        self.fields['subject'].queryset = Subject.objects.filter(user=user_id)
        self.fields['user'].queryset = User.objects.filter(
            groups__name__in=['students'])