from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm 
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from anket.models import Anket
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="/user/giris")
def kisisel(request):
    return render (request,"kisisel.html")

@login_required(login_url="/user/giris")
def sil(request):
    try:
        Anket.objects.filter(author_id=request.user.id).update(author_id="0")
        u = User.objects.get(username = request.user.username)
        u.delete()
        messages.success(request, "Kullanıcı Silinmiştir")   
        logout(request)
        return redirect('/')

    except User.DoesNotExist:
        messages.error(request, "Kullanıcı Mevcut değildir")    
        return redirect('/user/logout/')

    except Exception as e: 
        messages.error(request, e)    
        return redirect('/')

    return render(request, 'index.html') 

def kayıtol(request):
    if request.method=="POST":
        form=RegisterForm(request.POST )
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password = make_password(form.cleaned_data.get("password"))
            email=form.cleaned_data.get("email")
            first_name=form.cleaned_data.get("first_name")
            last_name=form.cleaned_data.get("last_name")
            
            newUser= User(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
            newUser.save()
            login(request,newUser, backend='User')
            messages.success(request,messages.INFO,"Kayıt Başarılı ")
            return render(request,"Kullanıcı_arayuzu.html")
            
        context={"form":form}
        return redirect (request,"Kullanıcı_arayuzu.html",context)
       
    else:
        form=RegisterForm()
        context={"form":form}
        return render (request,"kayıtol.html",context)

 
@login_required(login_url="/user/giris")
def kullanıcı_arayuzu(request):
    return render (request,"Kullanıcı_arayuzu.html")

def girisyap(request):
    form=LoginForm(request.POST or None)
    context={"form":form}
    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        user = authenticate(username=username,password=password)
        if user is None:
            messages.info(request,"Kullanıcı mevcut değil")
            return render(request,"giris.html",context)
        login(request,user)
        messages.success(request,"Giriş yapılmıştır.")
        if user.is_staff:
            return redirect('/admin')
        return redirect('/user/kullanıcı_arayuzu/')
        # (request,"kullanıcı_arayuzu.html",{"user":user})
    else:
        form=LoginForm()
        context={"form":form}
        return render (request,"giris.html",context)

@login_required(login_url="/user/giris")
def cıkıs(request):
    logout(request)
    messages.success(request,"Çıkış yapıldı")
    return redirect("/user/giris")

 