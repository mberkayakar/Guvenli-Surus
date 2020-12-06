from django.contrib import admin
from .models import İletisim 


 
class adminİletisim(admin.ModelAdmin):
    list_display=["Email","subject","message","logo"]
    list_display_links=["Email","subject","message","logo"]
    list_filter=["Email","subject","message","logo"]
    search_fields=["Email","subject","message","logo"]
    class Meta:
        model=İletisim
 


admin.site.register(İletisim ,adminİletisim)
 
 


  

 