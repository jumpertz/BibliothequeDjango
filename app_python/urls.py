from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.urls import path, include

from .views import index_views, user_views

urlpatterns = [
    path('', login_required(index_views.HomePageView.as_view()), name='index'),
    path('accounts/', include('django.contrib.auth.urls'), ),
    path('accounts/signup', index_views.SignUpView.as_view(), name='signup'),
    path('accounts/signin', index_views.SignInView.as_view(), name='signin'),
    path('accounts/edit', user_views.update_profile_view, name='user_update_profile'),

    path('users', user_views.index, name='index_users'),
    path('users/create', user_views.create_view, name='create_users'),
    path('users/update/<int:user_id>', user_views.update_view, name='update_users'),
    path('users/delete/<int:user_id>', user_views.delete, name='delete_users'),
    path('users/upload/', user_views.upload, name='upload_users')
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
