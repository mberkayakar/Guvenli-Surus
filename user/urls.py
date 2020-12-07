from django.contrib import admin
from django.urls import path,include
from user.views import kayıtol,kullanıcı_arayuzu,girisyap,cıkıs,sil,kisisel
from django.contrib.auth import views as auth_views 
 


app_name="user"

urlpatterns = [
    path('kayıtol/',kayıtol),
    path('kullanıcı_arayuzu/',kullanıcı_arayuzu),
    path('giris/',girisyap),
    path('logout/',cıkıs),
    path('sil/',sil),
    path('kisisel/',kisisel),
#   path('account/', include('django.contrib.auth.urls')),
#   path('password-reset/', auth_views.PasswordResetView.as_view( template_name='commons/password-reset/password_reset.html', subject_template_name='commons/password-reset/password_reset_subject.txt', email_template_name='commons/password-reset/password_reset_email.html', ), name='password_reset'),
#   path('password-reset/done/', auth_views.PasswordResetDoneView.as_view( template_name='commons/password-reset/password_reset_done.html' ), name='password_reset_done'),
#   path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view( template_name='commons/password-reset/password_reset_confirm.html'  ), name='password_reset_confirm'),
#   path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view( template_name='commons/password-reset/password_reset_complete.html' ), name='password_reset_complete'),

    path('reset_password/',auth_views.PasswordResetView.as_view()),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view()),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view()),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view()),
    



 




    
]
 
