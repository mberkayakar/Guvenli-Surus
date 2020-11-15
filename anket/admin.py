from django.contrib import admin
from .models import Anket 


 
class adminAnket(admin.ModelAdmin):
    list_display=["author","sorun","tarih"]
    list_display_links=["author","sorun","tarih"]
    list_filter=["author","sorun","tarih"]
    search_fields=["author","sorun","tarih"]
    class Meta:
        model=Anket
 


admin.site.register(Anket,adminAnket)
 

# Register your models here.
