from django.shortcuts import render, redirect
from .form import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.utils.crypto import get_random_string
import re
from django.conf import settings
from django.core.mail import send_mail
from django.utils.safestring import mark_safe

def check_valid(dic):
    dic = dic.copy()
    dic['email'] = str(dic['email']).lower()
    if re.fullmatch("[0-9]{8}@uap-bd.edu", dic["email"]):
        return True
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
        if check_valid(request.POST):
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
                messages.error(request, mark_safe("Check if the e-mail is valid or not.<br/>(Note: Only the users from UAP are allowed.)"))
        return redirect("main:signup")
    form = NewUserForm()
    return render (request=request, template_name="main/signup.html", context={"register_form":form})