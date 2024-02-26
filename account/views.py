from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin 
from .forms import *
from .token import account_activation_token
from .models import UserBase
from django.urls import reverse_lazy

@login_required(login_url='account:login') 
def dashboard(request):
    return render(request, 'account/user/dashboard.html')


@login_required(login_url='account:login') 
def edit_details(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)

        if user_form.is_valid():
            user_form.save()

    else:
        user_form = UserEditForm(instance=request.user)

    return render(request, 'account/edit_details.html', {'user_form':user_form} )


def login_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('store:home')
        else:
            return redirect('account:login')
        
    else:
        if request.user.is_authenticated:
            return redirect('store:home')
        else:
            return render(request, 'account/login.html')


@login_required(login_url='account:login') 
def logout_user(request):
    logout(request)
    return redirect('store:home')

def account_register(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.set_password(form.cleaned_data['password1'])
            user.save()

          
            send_activation_email(request, user)
            
        
            return render(request, 'account/email/email_verification_sent.html') 

    else:
        form = RegistrationForm()

    return render(request, 'account/register.html', {'form': form})

def send_activation_email(request, user):
    current_site = get_current_site(request)
    domain = current_site.domain
    subject = 'Activate your Account'
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = account_activation_token.make_token(user)
    activation_link = f'http://{domain}/account/activate/{uid}/{token}/'

    message = render_to_string('account/email/account_activation_email.html', {
        'user': user,
        'activation_link': activation_link,
    })
    
    send_mail(subject, message, None, [user.email])

def account_activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        User = get_user_model()
        user = User.objects.get(pk=uid)

    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return render(request, 'account/email/activation_success.html')
    else:
        return render(request, 'account/email/activation_invalid.html')
    



    
class UserPasswordChange(PasswordChangeView, LoginRequiredMixin):
    model = UserBase
    form_class = UserPasswordChangeForm
    template_name = 'account/change_password.html'
    success_url = reverse_lazy('store:home')