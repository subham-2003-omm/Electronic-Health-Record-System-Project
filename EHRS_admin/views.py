from django.shortcuts import render,redirect
from Register.models import Register_Master
from .models import adminprofile_master
# Create your views here.



def adminviewprofile(request):
    email=request.session.get('email')
    ob=Register_Master.objects.get(Email=email)
    obj=adminprofile_master.objects.get(email=ob)
    return render(request,'adminviewprofile.html',{'data':ob,"data1":obj})

def adminprofile(request):
    email=request.session.get('email')
    ob=Register_Master.objects.get(Email=email)
    if request.method=="POST":
        image_file=request.FILES["image"]
        document=request.FILES["upload_doc"]
        profile_update_obj,created=adminprofile_master.objects.get_or_create(email=ob)
        if image_file:
            profile_update_obj.Image=image_file
        if document:
            profile_update_obj.Document=document
        profile_update_obj.save()
        ob.Name=request.POST.get('name',ob.Name)
        ob.Email=request.POST.get('email',ob.Email)
        ob.Mob=request.POST.get('mob',ob.Mob)
        ob.Gender=request.POST.get('gender',ob.Gender)
        ob.Role_name=request.POST.get('role',ob.Role_name)
        ob.DOB=request.POST.get('dob',ob.DOB)
        ob.save()

        return redirect("adminviewprofile")
    return render(request,"adminprofile.html",{'user':ob})

def viewdata(request):
    ob=Register_Master.objects.all()
    if request.method=="POST":
        email=request.POST["email"]
        btn=request.POST["btn"]
        if btn=="Delete":
            Register_Master.objects.get(Email=email).delete()
            return redirect("viewdata")
        elif btn=="Edit":
            ob=Register_Master.objects.get(Email=email)
            return render(request,"edit.html" ,{'user':ob})
        
    return render(request,"viewdata.html",{'data':ob})





def update(request):
    if request.method=="POST":
        name=request.POST["name"]
        email=request.POST["email"]
        gender=request.POST["gender"]
        DOB=request.POST["dob"]
        mob=request.POST["mob"]
        status=request.POST["status"]
    status_val = 1 if request.POST["status"] == "Active" else 0
    Register_Master.objects.filter(Email=email).update(Name=name, Gender=gender, DOB=DOB, Mob=mob, Status=status_val)

        # ob=Register_Master.objects.filter(Email=email).update(Name=name,Gender=gender,DOB=DOB,Mob=mob,Status=status)


    return redirect("viewdata")
    
    return render(request,"viewdata.html")
def ahome(request):
    uname=request.session.get('name')
    return render(request,'ahome.html',{'Ahome':uname})