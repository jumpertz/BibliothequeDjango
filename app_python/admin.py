from django.contrib import admin

from .models import User, Book, Genre, BookGenre, Library, Bookseller, BookLibrary, BookUser, GroupUser

#admin.site.register(User)
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(BookGenre)
admin.site.register(Library)
admin.site.register(Bookseller)
admin.site.register(BookLibrary)
admin.site.register(BookUser)
admin.site.register(GroupUser)
