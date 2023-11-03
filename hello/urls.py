from django.urls import path
from . import views

urlpatterns = [
    # Create a URL pattern that captures two string parameters (first_name and last_name) from the URL.
    path('<str:first_name>/<str:last_name>', views.hello)
]
