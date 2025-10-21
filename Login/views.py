from django.shortcuts import render,redirect
from Register.models import Register_Master

# Create your views here.
def login(request):
    if request.method=="POST":
        Email=request.POST["email"]
        Pwd=request.POST["pwd"]
        try:
            ob=Register_Master.objects.get(Email=Email,Password=Pwd)
            request.session['name']=ob.Name
            request.session['email']=ob.Email
            if ob.Status==1:
                if ob.Role_name=="doctor":
                    return redirect("dhome")
                if ob.Role_name=="doctor":
                    return redirect("dhome")
                elif ob.Role_name=="patient":
                    return redirect("phome")
                elif ob.Role_name=="staff":
                    return redirect("shome")
                elif ob.Role_name=="ehrs_admin":
                    return redirect("ahome")
            else:
                return render(request,"login.html",{'msg':'waiting for the admin conformation...'})
            
        except Exception as e:
            return render(request,"login.html",{"msg":"invalid username or Password"+ str(e)})
        
    return render(request,"login.html")

