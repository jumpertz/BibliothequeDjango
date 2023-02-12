from django.shortcuts import render, redirect, get_object_or_404
from ..models import Book, BookLibrary
from ..forms.book_form import BookForm
from django.views import generic
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required


class Books(generic.TemplateView):

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.FILES = None
        self.method = None
        self.POST = None

    def book_list(request):
        books = Book.objects.all()
        return render(request, 'pages/books/index.html', {'books': books})

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
            title = self.POST['title']
            author = self.POST['author']
            thumbnail = self.FILES.get('thumbnail', None)
            description = self.POST['description']
            collection = self.POST['collection']
            idUer = self.user.id

            print (idUer)

            book = Book(title=title, author=author, thumbnail=thumbnail,
                        description=description, collection=collection)
            book.save()

            return redirect('index_books')

        return render(self, 'pages/books/new.html')

    @login_required
    def add_by_library(self, library_id):
        if self.method == "POST":
            title = self.POST['title']
            author = self.POST['author']
            thumbnail = self.FILES.get('thumbnail', None)
            description = self.POST['description']
            collection = self.POST['collection']

            book_library = BookLibrary.objects.get(pk=library_id)
            ## get the number of books in the library
            nb_books = book_library.book.count()
            book_library.book.add(Book.objects.get(pk=book_library.book.id))

            book = Book(title=title, author=author, thumbnail=thumbnail,
                        description=description, collection=collection)
            book.save()

            return redirect('index_books')

        return render(self, 'pages/books/new.html')

    @login_required
    def delete(self, id):
        Book.objects.filter(pk=id).delete()
        messages.success(self, "Le livre à bien été surprimée.")
        return redirect('index_books')

