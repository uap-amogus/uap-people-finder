from urllib import request
from django.shortcuts import render, redirect
from .form import NewUserForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.utils.crypto import get_random_string
import re
from django.conf import settings
from django.core.mail import send_mail
from django.utils.safestring import mark_safe
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

def check_valid(request, dic):
    dic = dic.copy()
    dic['email'] = str(dic['email']).lower()
    if re.fullmatch("[0-9]{8}@uap-bd.edu", dic["email"]):
        return True
    messages.error(request, mark_safe("Only the users from UAP are allowed. Use your UAP provided e-mail."))
    return False

def confirm_email(email, password):
    body = f"Hello There!\nYour Cerdentials at UAP PEOPLE FINDER\nemail = {email}\npassword = {password}"
    subject = 'Your Cerdentials at UAP PEOPLE'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email, ]
    send_mail( subject, body, email_from, recipient_list )
# Create your views here.

def signup_request(request):
    if request.method == "POST":
        if check_valid(request, request.POST):
            password = get_random_string(8)
            d = request.POST.copy()
            d['password1'] = password
            d['password2'] = password
            d['username'] = str(d['email']).lower()
            d['email'] = str(d['email']).lower()
            request.POST = d
            form = NewUserForm(request.POST)
            if form.is_valid():
                confirm_email(d['email'], password)
                form.save()
                messages.success(request, "An e-mail was sent to you with the credentials!" )
            else:   
                messages.error(request, mark_safe("An account already exist with this e-mail."))
        return redirect("main:signup")
    form = NewUserForm()
    return render (request=request, template_name="main/signup.html", context={"register_form":form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.info(request, "You are now logged in.")
                return redirect("main:login") #needs to be changed to profile page.
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="main/login.html", context={"login_form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect("main:login")

@login_required(login_url='main:login')
def profile_request(request):
    