from django.urls import path
from Staff import views    
urlpatterns = [
    path('',views.shome,name="shome"), 
    path('pdview/',views.patient_doctor_view,name="pdview"),
    path('add_test',views.add_test,name="add_test"),
    path('applytest',views.applytest,name="applytest"),
 ]