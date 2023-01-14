import csv
import io

from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import (get_object_or_404, render, redirect)

from ..forms.profile_form import ProfilForm
from ..forms.user_create_form import UserCreateForm
from ..forms.user_update_form import UserUpdateForm
from ..forms.user_upload_form import UploadFileForm


def index(request):
    _users = User.objects.all().order_by('username')

    return render(request, "pages/users/index.html", {"users": _users})


def update_profile_view(request):
    user = request.user

    if request.method == 'POST':
        form = ProfilForm(request.POST, instance=user)
        if form.is_valid():
            data = request.POST.dict()
            form.save()
            messages.success(
                request, "L'utilisateur {} à bien été modifiée".format(data['username']))
        else:
            messages.error(
                request, 'Il y a des erreurs dans le formulaire, veuillez vérifier.')
    else:
        form = UploadFileForm()
    return render(request, 'pages/profil/edit.html', {
        'form': form,
    })


def upload(request):
    if request.method == 'POST':
        print('file', request.FILES)
        form = UploadFileForm(files=request.FILES)
        print(form.is_valid())
        if form.is_valid():
            csv_file = request.FILES['file']
            # handle_uploaded_file(request.FILES['file'])
            data_set = csv_file.read().decode('UTF-8')
            io_string = io.StringIO(data_set)
            next(io_string)
            for column in csv.reader(io_string, delimiter=';', quotechar="|"):
                user = User.objects.create_user(
                    {
                        "username": column[0],
                        "first_name": column[1],
                        "last_name": column[2],
                        "password": column[3],
                        "groups": column[4],
                    }
                )
                user.save()

            return HttpResponse(data_set)
    else:
        form = UploadFileForm()
    return render(request, 'pages/users/upload.html', {'form': form})


def handle_uploaded_file(f):
    print(f)
    with open(f, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def create_view(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            data = request.POST.dict()
            user = form.clean()
            new_user = User.objects.create_user(user.get('first_name')[0] + user.get('last_name'), None,
                                                user.get('password'), first_name=user.get('first_name'),
                                                last_name=user.get('last_name'))
            new_user.groups.set(user.get('groups'))
            new_user.save()
            messages.success(
                request, "L'utilisateur {} à bien été créé.".format(new_user.username))
        else:
            messages.error(
                request, 'Il y a des erreurs dans le formulaire, veuillez vérifier')
    else:

        form = UserCreateForm()

    return render(request, 'pages/users/manage.html', {
        'form': form,
        'mode': 'C'
    })


def update_view(request, user_id):
    _user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=_user)
        if form.is_valid():
            data = request.POST.dict()
            user = form.save()
            messages.success(
                request, "L'utilisateur {} à bien été modifié".format(user.username))
        else:
            messages.error(
                request, 'Il y a des erreurs dans le formulaire, veuillez vérifier')
    else:

        form = UserUpdateForm(instance=_user)

    return render(request, 'pages/users/manage.html', {
        'form': form,
        'mode': 'U'
    })


def delete(request, user_id):
    User.objects.filter(pk=user_id).delete()
    messages.success(request, "L'utilisateur à bien été supprimé).")
    return redirect('index_users')
