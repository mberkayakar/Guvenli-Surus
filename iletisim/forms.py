from django import forms
from .models import İletisim
class İletisim(forms.ModelForm):
   class Meta():
      model=İletisim
      fields =["Email","subject","message","logo"]
   def clean(self):
      Email=self.cleaned_data.get('Email')
      subject=self.cleaned_data.get('subject')
      message=self.cleaned_data.get('message')
      logo=self.cleaned_data.get('logo')
      values={"Email":Email,"subject":subject,"message":message,"logo":logo}
      return values
        
