from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages
# Create your views here.

def kayıtol(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            email=form.cleaned_data.get("email")
            first_name=form.cleaned_data.get("first_name")
            last_name=form.cleaned_data.get("last_name")
            newUser= User(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
            newUser.save()
            login(request,newUser)
            messages.success(request,messages.INFO,"Kayıt Başarılı ")
            return render(request,"navigasyon.html")
            
        context={"form":form}
        return render (request,"kullanıcı_arayuzu.html",context)
       
    else:
        form=RegisterForm()
        context={"form":form}
        return render (request,"kayıtol.html",context)

 

def kullanıcı_arayuzu(request):
    return render (request,"kullanıcı_arayuzu.html")

def girisyap(request):
    return render (request,"giris_yap.html")