from django.shortcuts import render, redirect, get_object_or_404
from ..models import GroupUsers, GroupUser
from django.views import generic
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required


class ReadingGroups(generic.TemplateView):

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.FILES = None
        self.method = None
        self.POST = None

    def group_user_list(request):
        group_users = GroupUsers.objects.all()
        return render(request, 'pages/reading-groups/index.html', {'reading_groups': group_users})

    def search(request):
        if request.method == "POST":
            query = request.POST['search']
            group_users = GroupUsers.objects.filter(title__icontains=query)
            return render(request, 'pages/reading-groups/search.html', {'reading_groups': group_users})
        group_users = GroupUsers.objects.all()
        return render(request, 'pages/reading-groups/search.html', {'reading_groups': group_users})

    def details(self, id):
        group_user = get_object_or_404(GroupUsers, pk=id)
        return render(self, 'pages/reading-groups/details.html', {'reading_group': group_user})


    @login_required
    def add(self):
        if self.method == "POST":
            title = self.POST['title']
            organizer = self.user
            description = self.POST['description']
            start = self.POST['start']
            end = self.POST['end']

            group_users = GroupUsers(title=title, organizer=organizer, description=description, start=start, end=end)
            group_users.save()

            return redirect('index_group_users')

        return render(self, 'pages/reading-groups/new.html')


    @login_required
    def join(self, id):
        group_user = get_object_or_404(GroupUsers, pk=id)
        user = self.user
        group_user.user.add(user)
        return redirect('index_group_users')


    @login_required
    def delete(self, id):
        GroupUsers.objects.filter(pk=id).delete()
        messages.success(self, "Le groupe de lecture a bien été supprimé.")
        return redirect('index_group_users')

