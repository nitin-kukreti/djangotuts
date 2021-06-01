
from .views import detailspage, home, registercar
from django.http.response import HttpResponse
from django.urls.conf import path


urlpatterns=[
    path("",home),
    path('register',registercar),
    path('detail/<int:pk>/',detailspage)
]