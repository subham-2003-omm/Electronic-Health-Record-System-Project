from django.shortcuts import render,get_object_or_404,redirect
from Register.models import Register_Master
from Patient.models import Doctor_Appointment
from .models import *
from django.contrib import messages
# Create your views here.
def dhome(request):
    uname=request.session.get('name')
    return render(request,'dhome.html',{'Dhome':uname})

def patientviewdata(request):
    ob=Register_Master.objects.filter(Role_name="patient")
    # ob1=Register_Master.objects.filter(Role_name="staff")
    return render(request,"patientviewdata.html",{'pdata':ob})


def display_appointment(request):
    email=request.session.get("email")
    ob=Register_Master.objects.get(Email=email)
    ob1=Doctor_Appointment.objects.filter(doct_email=ob)
    # ob2=Doctor_Appointment.objects.all()
    return render(request,"appointment_details.html",{"appointment":ob1})

def approve_appointment(request):
    if request.method == "POST":
        appointment_id=request.POST.get("appointment_id")
        appointment=get_object_or_404(Doctor_Appointment,id=appointment_id)
        appointment.status= "Approved"
        appointment.save()
        messages.success(request, f"Appointment for{appointment.p_name}has been approved.")
        return redirect('display_appointment')
    
def cancel_appointment(request):
    if request.method == "POST":
        appointment_id=request.POST.get("appointment_id")
        appointment=get_object_or_404(Doctor_Appointment,id=appointment_id)
        appointment.status= "Cancelled"
        appointment.save()
        messages.error(request, f"Appointment for{appointment.p_name}has been cancelled.")
        return redirect('display_appointment')
    
# def viewdetails(request):
#     if request.method=="POST":
#         pid=request.POST["pid"]
#         btn=request.POST["btn"]

#         if btn=="ViewDetails":
#             ob= Doctor_Appointment.objects.get(id=pid)
#             return render(request,"patient_details.html",{"pdata":ob})
#         elif btn == "submit":
#             prescription_text=request.POST["prescription"]
#             app= Doctor_Appointment.objects.get(id=pid)

#             Precription.objects.create(
#                 app_id=app,
#                 prescription_text=prescription_text
#             )
        
#             return redirect("display_appointment")

#     return redirect("display_appointment")





def viewdetails(request):
    if request.method == "POST":
        pid = request.POST.get("pid")
        btn = request.POST.get("btn")  

        if btn == "ViewDetails":
            ob = Doctor_Appointment.objects.get(id=pid)
            return render(request, "patient_details.html", {"pdata": ob})
        elif btn == "submit":
            prescription_text = request.POST.get("prescription", "")
            app = Doctor_Appointment.objects.get(id=pid)
            Precription.objects.create(
                app_id=app,
                prescription_text=prescription_text
            )
            return redirect("display_appointment")

    return redirect("display_appointment")
