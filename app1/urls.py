
from django.urls import path
from .views import *
urlpatterns=[
   path('',homePage),
   path('contact',contact),
   path('about',about),
   path('signup',signup),
   path('register',registeruser,name="register"),
]