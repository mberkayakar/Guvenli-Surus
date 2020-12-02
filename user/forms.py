from django import forms


class RegisterForm(forms.Form):
    username=forms.CharField(max_length=50,label='Kullanıcı Adı')
    first_name=forms.CharField(max_length=50,label='İsim')
    last_name=forms.CharField(max_length=50,label='Soyisim')
    password=forms.CharField(max_length=20,label='Şifre',widget = forms.PasswordInput)
    confirm=forms.CharField(max_length=20,label='Şifreyi Tekrar Giriniz',widget = forms.PasswordInput)
    email = forms.EmailField(label="lütfen email giriniz ( zorunlu değil)",required=False)
    def clean(self):
        username=self.cleaned_data.get('username')
        password=self.cleaned_data.get('password')
        confirm=self.cleaned_data.get('confirm')
        first_name=self.cleaned_data.get('first_name')
        last_name=self.cleaned_data.get('last_name')
        email=self.cleaned_data.get('email')
        if password and confirm and password!=confirm:
            raise forms.ValidationError("Parolalar eşleşmemektedir")     #exeptions fırlatır
        
        values={"username":username,"password":password,"email":email,"first_name":first_name,"last_name":last_name}
        return values
        