from django.db import models
from django.utils.timezone import now # 
import datetime

# Create your models here.


class Anket(models.Model):    #anket tablom
    author = models.ForeignKey("auth.user",on_delete=models.CASCADE,verbose_name="Kayıdı oluşturan")   # kimin yazacagını userdaki foreing ile  tutacaz 
    enlem  = models.FloatField()
    boylam = models.FloatField()
    sorun  = models.CharField(max_length=50)

    #kazamı yoksa kaza riskimi var
    ana_unsur = models.CharField(max_length=50 ,verbose_name="Sorun Kim Tarafından Kaynaklı") # belediye / kullanıcılar / doğal problemler vs
    benzerlik = models.CharField(max_length=50, verbose_name="Hangi Guruba Dahil") # belediyenin alt yapılandırması mesela trafik işaretçilerimi yoksa asvaltmı vs
    alinabilecek_onlem = models.TextField( verbose_name="Sorun ve Çözüm İçin Tavsiyeler")
    tarih = models.DateTimeField(default=now, editable=False)  
 
 

#   def __str__(self):
#       return self.author

