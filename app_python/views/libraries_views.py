from django.shortcuts import render, redirect, get_object_or_404

from ..models import Library, BookLibrary, Bookseller

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

            libraries = Library.objects.filter(title__icontains=query)
            return render(request, 'pages/libraries/search.html', {'libraries': libraries})
        libraries = Library.objects.all()
        return render(request, 'pages/libraries/search.html', {'libraries': libraries})

    def details(self, id):
        library = get_object_or_404(Library, pk=id)
        return render(self, 'pages/libraries/details.html', {'library': library, 'books': BookLibrary.objects.filter(library=library)})



    @login_required
    def add(self):
        if self.method == "POST":

            name = self.POST['name']
            address = self.POST['address']
            city = self.POST['city']
            zipcode = self.POST['zipcode']
            country = self.POST['country']

            owner_id = self.user.id
            
            library = Library(name=name, address=address, city=city,
                        zipcode=zipcode, country=country, owner_id=owner_id)
            library.save()


            bookseller = Bookseller(library=library, user=self.user)
            bookseller.save()


        return render(self, 'pages/libraries/new.html')

    @login_required
    def delete(self, id):

        Library.objects.filter(pk=id).delete()
        messages.success(self, "La librairie à bien été supprimée.")
        return redirect('library_list')


