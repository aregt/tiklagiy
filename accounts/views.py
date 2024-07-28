from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm

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
                messages.error(request,"Geçersiz kullanıcı adı veya şifre.")
        else:
            messages.error(request,"Geçersiz kullanıcı adı veya şifre.")
    form = CustomAuthenticationForm()
    return render(request=request, template_name="accounts/login.html", context={"login_form":form})