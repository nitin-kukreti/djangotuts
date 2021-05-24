from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def homePage(request):
    # return render(request,template_name='hompage.html',context={'data':"nitin","id":1})
    return render(request,'hompage.html',{'data':"nitin","id":1})

def contact(request):
    return HttpResponse("this is contact page")

def about(request):
    return render(request,'about.html',{'name':"nitin"})