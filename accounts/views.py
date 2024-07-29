from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth.views import LogoutView
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from .models import CustomUser

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Kullanıcıyı deaktif olarak kaydet
            user.save()
            send_verification_email(request, user)
            messages.success(request, f"Hoş geldiniz, {user.username}! Hesabınız oluşturuldu. Lütfen e-postanızı kontrol edin ve hesabınızı doğrulayın.")
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def send_verification_email(request, user):
    token = user.email_verification_token
    verify_url = request.build_absolute_uri(reverse('verify_email', args=[token]))
    subject = 'E-posta Adresinizi Doğrulayın'
    message = f'Merhaba {user.username},\n\nHesabınızı doğrulamak için lütfen aşağıdaki bağlantıya tıklayın:\n\n{verify_url}'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [user.email]
    send_mail(subject, message, from_email, recipient_list)

def verify_email(request, token):
    try:
        user = CustomUser.objects.get(email_verification_token=token)
        user.is_active = True
        user.email_verified = True
        user.email_verification_token = ''
        user.save()
        login(request, user)
        messages.success(request, 'E-posta adresiniz başarıyla doğrulandı.')
        return redirect('home')
    except CustomUser.DoesNotExist:
        messages.error(request, 'Geçersiz doğrulama bağlantısı.')
        return redirect('login')

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.email_verified:
                    login(request, user)
                    messages.info(request, f"Hoş geldiniz, {username}!")
                    return redirect('home')
                else:
                    messages.error(request, "Lütfen önce e-posta adresinizi doğrulayın.")
            else:
                messages.error(request, "Geçersiz kullanıcı adı veya şifre.")
        else:
            messages.error(request, "Geçersiz kullanıcı adı veya şifre.")
    else:
        form = CustomAuthenticationForm()
    return render(request=request, template_name="accounts/login.html", context={"login_form": form})