
from .views import home, registercar
from django.http.response import HttpResponse
from django.urls.conf import path


urlpatterns=[
    path("",home),
    path('register',registercar)
]