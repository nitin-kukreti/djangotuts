from django.shortcuts import render
from django.http.response import HttpResponse
import json;
# Create your views here.
def homePage(request):
    # return render(request,template_name='hompage.html',context={'data':"nitin","id":1})
    return render(request,'hompage.html',{'data':"nitin","id":1})

def contact(request):
    return HttpResponse("this is contact page")

def about(request):
    return render(request,'about.html',{'name':"nitin"})

def signup(request):
    return render(request,"signup.html")

def registeruser(req):
    commingdata=req.GET
    userdata={
        "username":commingdata.get("username"),
        "pasword":commingdata.get("pasword")
    }
    print(commingdata)
    with open("mydata.json","r") as f:
        data=json.loads(f.read())
        a=data.get("users")
        print(a)
        print(type(a))
        data.get("users").append(userdata)
        print(data)
        with open("mydata.json","w") as f:
            f.write(json.dumps(data))

    return  HttpResponse("data is saved")  