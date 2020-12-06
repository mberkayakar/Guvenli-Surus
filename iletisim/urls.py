from django.contrib import admin
from django.urls import path 
from iletisim.views import iletisim

app_name ="iletisim"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('iletisim/',iletisim),

]   