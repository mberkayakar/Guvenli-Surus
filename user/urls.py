from django.contrib import admin
from django.urls import path
from user.views import kayıtol,kullanıcı_arayuzu,girisyap

app_name="user"

urlpatterns = [
    
    
    path('kayıtol/',kayıtol),
    path('kullanıcı_arayuzu/',kullanıcı_arayuzu),
    path('giris_yap/',girisyap),
    

]   
