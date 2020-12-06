from django.db import models
from django.core.mail import send_mail
 
# Create your models here.
class İletisim(models.Model):    #anket tablom
    Email = models.EmailField(verbose_name="lütfen Sizinle iletişime geçebilmemiz adına gereçli bir e posta adresi giriniz",max_length=50)
    subject = models.CharField(verbose_name="Hangi konu hakkında bizimle ilerişime geçmek istersiniz ?",max_length=50)
    message = models.CharField(verbose_name="mesajınızı bize detaylı olarak anlatınız",max_length=50)
    logo = models.ImageField(blank=True, upload_to='')


    