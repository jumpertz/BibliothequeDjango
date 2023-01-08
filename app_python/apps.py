from django.apps import AppConfig


class LibrariesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'libraries'


class AppPythonConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_python'
    verbose_name = 'App Python'
