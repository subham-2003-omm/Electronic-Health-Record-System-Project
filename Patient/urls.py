from django.urls import path
from Patient .views import phome,dsviewdata,take_appoinment,success,patient_dasboard,viewlabtest,testreport
urlpatterns = [
    path('',phome,name="phome"), 
    path('dsview/',dsviewdata,name="dsview"),
    path('takeappointment',take_appoinment,name="takeappointment"),
    path('success',success,name="success"),
    path('patient_dasboard',patient_dasboard,name='patient_dasboard'),
    path('viewlabtest',viewlabtest,name='viewlabtest'),
     path("testreport", testreport, name="testreport")
 ]