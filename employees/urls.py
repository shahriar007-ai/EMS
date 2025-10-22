from django.urls import path
from django.http import HttpResponse

def placeholder(request):
    return HttpResponse("Employees API placeholder.")

urlpatterns = [
    path("", placeholder),
]
