from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

from ..models import Book


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class HomePageView(generic.TemplateView):
    template_name = 'pages/home.html'


class SignInView(LoginView):
    template_name = 'registration/login.html'
    form_class = AuthenticationForm
    redirect_field_name = 'home'

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


class Books(generic.TemplateView):

    def book_list(request):
        books = Book.objects.all()
        return render(request, 'books/index.html', {'books': books})

    def add(request):
        if request.method == "POST":
            title = request.POST['title']
            author = request.POST['author']
            thumbnail = request.FILES['thumbnail']
            description = request.POST['description']
            collection = request.POST['collection']

            book = Book(title=title, author=author, thumbnail=thumbnail,
                        description=description, collection=collection)
            book.save()

            return redirect('index_books')

        return render(request, 'books/new.html')

    def search(request):
        if request.method == "POST":
            query = request.POST['search']
            books = Book.objects.filter(title__icontains=query)
            return render(request, 'books/search.html', {'books': books})
        books = Book.objects.all()
        return render(request, 'books/search.html', {'books': books})
