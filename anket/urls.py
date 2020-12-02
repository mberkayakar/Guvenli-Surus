from django.contrib import admin
from django.urls import path 
from anket.views import anketekle

app_name ="anket"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('anketekle',anketekle)
]   