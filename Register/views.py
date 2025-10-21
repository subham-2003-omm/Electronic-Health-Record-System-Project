from django.shortcuts import render
from .models import Register_Master
# Create your views here.
def signup(request):
    if request.method=="POST":
        username=request.POST["name"]
        email=request.POST["email"]
        mob=request.POST["mob"]
        password=request.POST["password"]
        gender=request.POST["gender"]
        address=request.POST["adds"]
        dob=request.POST["dob"]
        role_name=request.POST["role"]
        ob=Register_Master.objects.create(Name=username,Email=email,Mob=mob,Password=password,DOB=dob,Gender=gender,Address=address,Role_name=role_name)
        ob.save()

        return render(request,"signup.html",{'msg':"Register successfull"})
    return render(request,"signup.html")
