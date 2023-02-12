from django.shortcuts import (get_object_or_404,
                              render,
                              redirect)
from django.views import generic
from django.contrib.auth.decorators import user_passes_test


class Admin(generic.TemplateView):

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.is_superuser = None

    def superuser_only(self):
        return self.is_superuser

    @user_passes_test(superuser_only)
    def index(request):
        return render(request, 'admin/index.html')
