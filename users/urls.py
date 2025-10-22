# users/urls.py
from django.urls import path
from django.http import HttpResponse

def api_placeholder(request):
    return HttpResponse("Users API placeholder.")

urlpatterns = [
    path("", api_placeholder),
]
