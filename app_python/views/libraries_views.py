from django.shortcuts import render, redirect, get_object_or_404
from ..models import Library
from ..forms.book_form import BookForm
from django.views import generic
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required


class Libraries(generic.TemplateView):

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.FILES = None
        self.method = None
        self.POST = None

    def libraries_list(self):
        libraries = Library.objects.all()
        return render(self, 'pages/libraries/index.html', {'libraries': libraries})

    def search(request):
        if request.method == "POST":
            query = request.POST['search']
            books = Book.objects.filter(title__icontains=query)
            return render(request, 'pages/books/search.html', {'books': books})
        books = Book.objects.all()
        return render(request, 'pages/books/search.html', {'books': books})

    def details(self, id):
        book = get_object_or_404(Book, pk=id)
        return render(self, 'pages/books/details.html', {'book': book})


    @login_required
    def add(self):
        if self.method == "POST":
            name = self.POST['name'],
            address = self.POST['address'],
            city = self.POST['city'],
            zipcode = self.POST['zipcode'],
            country = self.POST['country'],
            owner_id = self.user.id
            
            library = Library(name=name, address=address, city=city,
                        zipcode=zipcode, country=country, owner_id=owner_id)
            library.save()
        return render(self, 'pages/libraries/new.html')

    @login_required
    def delete(self, id):
        Book.objects.filter(pk=id).delete()
        messages.success(self, "Le livre à bien été surprimée.")
        return redirect('index_books')

