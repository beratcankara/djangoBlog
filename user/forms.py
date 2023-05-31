from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
class LoginForm(forms.Form):
    userName = forms.CharField(label="Lütfen kullanıcı adınızı giriniz.", max_length=50)
    userPass = forms.CharField(widget=forms.PasswordInput, max_length=20, label="Lütfen şifre giriniz.")
    
class RegisterForm(forms.Form):
    userName = forms.CharField(label="Lütfen kullanıcı adınızı giriniz.", max_length=50)
    userPass = forms.CharField(widget=forms.PasswordInput, max_length=20, label="Lütfen şifre giriniz.")
    checkPass = forms.CharField(widget=forms.PasswordInput, max_length=20, label="Lütfen şifrenizi doğrulayın.")
    
    def clean(self):
        cleaned_data = super().clean()
        userName = cleaned_data.get("userName")
        userPass = cleaned_data.get("userPass")
        checkPass = cleaned_data.get("checkPass")
        
        if userPass and checkPass and userPass != checkPass:
            self.add_error("checkPass", "Parolalar eşleşmiyor.")

        if userName and User.objects.filter(username=userName).exists():
            self.add_error("userName", "Bu kullanıcı adı zaten kullanılıyor.")

        return cleaned_data
    
    def save(self):
        userName = self.cleaned_data.get("userName")
        userPass = self.cleaned_data.get("userPass")
        
        newUser = User(username=userName)
        newUser.set_password(userPass)
        newUser.save()
        
        return newUser