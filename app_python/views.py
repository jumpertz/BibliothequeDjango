from django.shortcuts import render, redirect
from django.contrib.auth import authenticate

from .models import User
from .registerForm import SignUpForm


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request)
            return redirect('home')
        else:
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    logout(request)
    return redirect('login')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            phone = form.cleaned_data.get('phone')
            # Do something with the cleaned data, like creating a user object
            user = User.objects.create(
                name=name, email=email, password=password, phone=phone
            )
        else:
            # code pour gérer le cas où le formulaire n'est pas valide
            return render(request, 'register.html', {'form': form})
        return render(request, 'login.html', {'form': form})
