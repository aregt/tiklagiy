from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth.views import LogoutView

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Hoş geldiniz, {user.username}! Hesabınız başarıyla oluşturuldu.")
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Hoş geldiniz, {username}!")
                return redirect('home')
            else:
                messages.error(request, "Geçersiz kullanıcı adı veya şifre.")
        else:
            messages.error(request, "Geçersiz kullanıcı adı veya şifre.")
    else:
        form = CustomAuthenticationForm()
    return render(request=request, template_name="accounts/login.html", context={"login_form": form})