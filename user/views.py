from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request,"Başarıyla kayıt olundu.")
            return redirect("index")
        else:
            context = {
                "form": form
            }
            return render(request, "register.html", context=context)
    else:
        form = RegisterForm()
        context = {
            "form": form
        }
        return render(request, "register.html", context=context)

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            userName = form.cleaned_data.get("userName")
            userPass = form.cleaned_data.get("userPass")
            user = authenticate(request, username=userName, password=userPass)
            if user is not None:
                auth_login(request,user)
                messages.success(request,"Başarıyla giriş yapıldı.")
                return redirect("index")  # Giriş başarılı, yönlendirme yapabilirsiniz
            else:
                messages.error(request, "Geçersiz kullanıcı adı veya şifre")  # Hata mesajını kullanıcıya göstermek için messages framework'ünü kullanın
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})
@login_required(login_url="/user/login")
def logoutUser(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Başarıyla çıkış yapıldı.")
        return redirect("index")
    else:
        messages.error(request,"Oturum açılmamış kullanıcılar çıkış yapamaz.")
    return redirect("index")