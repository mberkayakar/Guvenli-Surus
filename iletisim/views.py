from datetime import datetime

from django.shortcuts import render
from guvenlisurus.settings import EMAIL_HOST_USER
from .forms import İletisim
from django.core.mail import EmailMessage #send_mail

from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os

# Create your views here.

def iletisim(request):
    form = İletisim(request.POST, request.FILES or None)
    if request.method == 'POST' and request.FILES['logo']:
        
        if form.is_valid():
            # form = İletisim(request.POST, request.FILES or None)

            form.save()

            
                        
            logo = request.FILES['logo']
            fs = FileSystemStorage()
            # logo.name = request.user.username+"-"+guvenlisurus_eposta+"-"+str(datetime.now().strftime("%d_%m_%Y-%H_%M_%S"))+logo.name
            
            filename = fs.save(logo.name, logo)
            # uploaded_file_url = fs.url(filename)
            
            oto_subject = 'Talebiniz Alınmıştır'
            oto_message = 'Merhabalar Güvenli sürüş ailesi olarak elimizden gelen emeği sarf ediyoruz bildirminiz için çok teşekkür eder, iyi günler dileriz ...  '
            recepient = str(form['Email'].value())
            try:
                mail = EmailMessage(oto_subject, oto_message, EMAIL_HOST_USER, [recepient])
                filename = os.path.join(settings.MEDIA_ROOT, logo.name)
         
                mail.attach_file(filename)
                mail.send()
            except Exception as e:
                print(e)
                return render(request, 'hakkında.html', {'recepient': recepient, 'error_message': 'Either the attachment is too big or corrupt'})


            # send_mail(oto_subject,oto_message, EMAIL_HOST_USER, [recepient], fail_silently = False)
          
            guvenlisurus_eposta=form.cleaned_data.get("Email")
            subject = form.cleaned_data.get("subject")
            message = form.cleaned_data.get("message")
            try:
                
                filename = os.path.join(settings.MEDIA_ROOT, logo.name)
                mail = EmailMessage(oto_subject, oto_message, EMAIL_HOST_USER, [guvenlisurus_eposta])
                mail.attach_file(filename)
                mail.send()
            except:
                return render(request, 'hakkında.html', {'recepient': recepient, 'error_message': 'Either the attachment is too big or corrupt'})

         
            # send_mail(subject,message, EMAIL_HOST_USER, [guvenlisurus_eposta], fail_silently = False)
            return render(request, 'hakkında.html', {'recepient': recepient})


            





    return render(request, 'iletisim.html', {'form':form})
 

 