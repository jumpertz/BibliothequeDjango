from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.contrib.auth.decorators import user_passes_test

from .views import index_views, user_views, book_views, admin_views, libraries_views , topic_views


def superuser_only(user):
    return user.is_superuser


urlpatterns = [
    # ADMIN

    path('', book_views.Books.book_list, name='index_books'),
    # path('', login_required(index_views.HomePageView.as_view()), name='index'),
    path('accounts/', include('django.contrib.auth.urls'), ),
    path('accounts/signup', index_views.SignUpView.as_view(), name='signup'),
    path('accounts/signin', index_views.SignInView.as_view(), name='signin'),
    path('accounts/edit', user_views.update_profile_view, name='user_update_profile'),

    # USERS
    path('users', user_views.index, name='index_users'),
    path('users/create', user_views.create_view, name='create_users'),
    path('users/update/<int:user_id>', user_views.update_view, name='update_users'),
    path('users/delete/<int:user_id>', user_views.delete, name='delete_users'),

    # BOOKS
    path('books/', book_views.Books.book_list, name='index_books'),
    path('books/<int:id>/', book_views.Books.details, name='details_book'),
    path('books/new', book_views.Books.add, name='new_book'),
    path('books/search', book_views.Books.search, name='search_books'),
    path('books/delete/<int:id>/', book_views.Books.delete, name='delete_book'),

    # LIBRARY
    path('libraries/', libraries_views.Libraries.libraries_list, name='library_list'),
    path('libraries/new', libraries_views.Libraries.add, name='new_library'),

    # TOPIC 
    path('topics/', topic_views.Topics.topic_list, name='index_topics'),
    path('topics/<int:id>/', topic_views.Topics.details, name='details_topic'),
    path('topics/new', topic_views.Topics.add, name='new_topic'),
    path('topics/search', topic_views.Topics.search, name='search_topics'),
    path('topics/delete/<int:id>/', topic_views.Topics.delete, name='delete_topic'),



]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
