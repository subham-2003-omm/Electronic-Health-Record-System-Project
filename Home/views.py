from django.shortcuts import render,HttpResponse
from .models import Contact_master

# Create your views here.
def gallary(request):
    return render(request,'gallary.html')
def faq(request):
    return render(request,'faq.html')
def contect(request):
    if request.method=="POST":
        Name=request.POST["name"]
        Email=request.POST["email"]
        Message=request.POST["msg"]
        ob=Contact_master.objects.create(name=Name,Email=Email,message=Message)
        ob.save()
        return render(request,"contect.html",{"msg":"store sucessfull....."})
    return render(request,"contect.html")
def about(request):
    return render(request,'about.html')
def home(request):
    return render(request,"home.html")


def add(request):
    if request.method=="POST":
        a=request.POST['fno']
        b=request.POST['sno']
        result=int(a)+int(b)
        return render(request,"add.html",context={"output":result})
    return render(request,"add.html")


def index(request):
    return HttpResponse("<h1>welcome to Django's World....</h1>")
