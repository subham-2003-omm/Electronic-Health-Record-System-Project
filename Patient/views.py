from django.shortcuts import render,redirect
from Register.models import Register_Master
from datetime import datetime
from Staff.models import Labratory_test
from .models import Doctor_Appointment
from .models import PatientTestReport



def testreport(request):
    report_id=request.session.get("last_report_id")
    report=PatientTestReport.objects.get(pk=report_id)

    return render(request,"testreport.html",{
        "report":report,
        "tests":report.tests.all(),
        "total_price":report.total_price
    })

def viewlabtest(request):
    email=request.session.get("email")
    logged_in_user=Register_Master.objects.get(Email=email)
    if request.method=="POST":
        selected_ids=request.POST.getlist("selected_tests")
        patient=logged_in_user
        tests=Labratory_test.objects.filter(test_id__in=selected_ids)
        total_price=sum(test.test_Price for test in tests)
        report=PatientTestReport.objects.create(patient=patient,total_price=total_price)
        report.tests.set(tests)
        report.save()
        request.session["last_report_id"] = report.report_id
        return redirect("testreport")
    ob=Labratory_test.objects.all()
    return render(request,"viewlabtest.html",{"testdata":ob,"user":logged_in_user})

def patient_dasboard(request):
     Appoinment=""
     if request.method=="POST":
          pmobile=request.POST["pmobile"]
          if pmobile:
               Appoinment=Doctor_Appointment.objects.filter(p_mobile=pmobile)
     return render(request,"patient_dasboard.html",{"msg":Appoinment})

def take_appoinment(request):
    if request.method=="POST":
         doct_name=request.POST["dname"]
         doct_email=request.POST["demail"]
         demail=Register_Master.objects.get(Email=doct_email)
         doct_mobile=request.POST["dmobile"]
         p_name=request.POST["pname"]
         p_mobile=request.POST["pmobile"]
         p_email=request.POST["pemail"]
         p_dob=request.POST["pdob"]
         p_address=request.POST["paddress"]
         p_gender=request.POST["pgender"]
         diseases=request.POST["disease"]
         ob=Doctor_Appointment.objects.create(
              doct_name = doct_name,
              doct_contact = doct_mobile,
              doct_email = demail,
              p_name = p_name,
              p_mobile = p_mobile,
              p_address = p_address,
              p_gender = p_gender,
              dob = p_dob,
              p_disease = diseases,
         )
         ob.save()
         return redirect("success")

         
        
    return render(request,'book_appointment.html')
def success(request):
    return render(request,"success_page.html")

def dsviewdata(request):
    ob=Register_Master.objects.filter(Role_name="doctor")
    if request.method=="POST":
        demail=request.POST["email"]
        btn=request.POST["btn"]
        if btn=="Appointment":
            obj=Register_Master.objects.get(Email=demail)
            pemail=request.session.get('email')
            obj1=Register_Master.objects.get(Email=pemail)
            return render(request,'book_appointment.html',{'Ddata':obj,'pdata':obj1})
            
                
    return render(request,"dsviewdata.html",{'ddata':ob})



def phome(request):
    uname=request.session.get('name')
    return render(request,'phome.html',{'Pname':uname})