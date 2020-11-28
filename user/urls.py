from django.contrib import admin
from django.urls import path
from user.views import kayıtol,kullanıcı_arayuzu

app_name="user"

urlpatterns = [
    
    
    path('kayıtol/',kayıtol),
    path('kullanıcı_arayuzu/',kullanıcı_arayuzu),
    

]   
