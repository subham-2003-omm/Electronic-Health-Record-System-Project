from django.shortcuts import render,redirect
from Register.models import Register_Master
from .forms import testForm
from Patient.models import *
# Create your views here.
def applytest(request):
    ob=PatientTestReport.objects.all()
    return render(request,"applytest.html",{'rdata':ob})

def add_test(request):
    formobj=testForm()
    if request.method=="POST":
        formobj=testForm(request.POST)
        if formobj.is_valid():
            formobj.save()
    return render(request,'Add_test.html',{'form':formobj})

def shome(request):
    uname=request.session.get('name')
    return render(request,'shome.html',{'Sname':uname})
def patient_doctor_view(request):
    ob=Register_Master.objects.filter(Role_name="patient")
    ob1=Register_Master.objects.filter(Role_name="doctor")
    
    return render(request,"pdviewdata.html",{'pdata':ob,"ddata":ob1})




