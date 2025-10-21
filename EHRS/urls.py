"""
URL configuration for EHRS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from Home import views as hviews
from Register import views as rviews
from Login import views as lviews
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #doctor
    path('doctor/',include('Doctor.urls')),

    #ehrs_admin
     path('ehrs_admin/',include('EHRS_admin.urls')),

    #patient
     path('patient/',include('Patient.urls')),

    #staff
     path('staff/',include('Staff.urls')),
    
    path('admin/', admin.site.urls),
    #Login
    path('signin/',lviews.login,name="Signin"),
    
    #Register
    path('signup/',rviews.signup,name="signup"),
    #Home
    path('',hviews.home,name="home"),
    path('about/',hviews.about,name="about"),
    path('contect/',hviews.contect,name="contect"),
    path('faq/',hviews.faq,name="faq"),
    path('gallary/',hviews.gallary,name="gallary"),
    path('add/',hviews.add,name='add'),
    





    path('index',hviews.index,name="index"),   
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)