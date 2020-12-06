from django.contrib import admin
from django.urls import path 
from anket.views import anketekle,anketyonetimi,anketislem,anketdetay

app_name ="anket"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('anketekle/',anketekle),
    path('anketyonetimi/',anketyonetimi),
    path('anketislem/',anketislem),
    path('detay/<int:id>',anketdetay),
    

]   