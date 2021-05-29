from app1.models import Student
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

def login(request):
    commingdata=request.GET
    userdata={
        "username":commingdata.get("username"),
        "pasword":commingdata.get("pasword")
    }
    if userdata.get("username") and userdata.get("pasword"):
        with open("mydata.json","r") as f:
            data=json.loads(f.read())
            if userdata in data.get("users"):
                sendata={
                    "message":"login sucess",
                    "login":True,
                    "username":commingdata.get("username"),
                    "pasword":commingdata.get("pasword")
                }
            else:
                sendata={"message":"login failed"}
        return render(request,"loginresult.html",sendata)
    return render(request,'login.html')   

def deleteuser(request,username,pasword):
        userdata={
         "username":username,
          "pasword":pasword
         }
        with open("mydata.json","r") as f:
            data=json.loads(f.read())
            users=data.get("users")
            if userdata in users:
                data.get("users").remove(userdata)
                with open("mydata.json","w") as f:
                    f.write(json.dumps(data))
                return HttpResponse("deleted")
            else:
               return HttpResponse("invalid request")

