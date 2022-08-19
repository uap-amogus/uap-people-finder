from django.shortcuts import render, redirect
from .form import NewUserForm, ProfileForm
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
from django.forms.models import model_to_dict
from main.models import Profile, ListofInterests, Interest
from django.contrib.auth.models import User




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
                user = form.save()
                Profile.objects.create(username=user, first_name='', last_name='')
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
                return redirect("main:profile") #needs to be changed to profile page.
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
    if request.method == "POST":
        d = request.POST
        profile_obj = Profile.objects.get(username=User.objects.get(username=str(request.user)))
        profile_obj.first_name = d['first_name']
        profile_obj.last_name = d['last_name']
        profile_obj.save()
        Interest.objects.filter(username=User.objects.get(username=str(request.user))).delete()
        d = d.copy()
        for i in range(1, 4):
            k = 'interest_'+str(i)
            if d[k] == "":
                d[k] = None
        try:
            Interest.objects.create(username=User.objects.get(username=str(request.user)), interest1=d['interest_1'], bio=d['interest_1_bio'], link=d['interest_1_link'])
            Interest.objects.create(username=User.objects.get(username=str(request.user)), interest1=d['interest_2'], bio=d['interest_2_bio'], link=d['interest_2_link'])
            Interest.objects.create(username=User.objects.get(username=str(request.user)), interest1=d['interest_3'], bio=d['interest_3_bio'], link=d['interest_3_link'])
        except:
            messages.error(request, "Invalid Interest Selection. (Must be unique.)")
            return redirect("main:profile")
        messages.success(request, "Successfully updated profile info!" )
        return redirect("main:profile")
        
    prefill_dict = model_to_dict(Profile.objects.get(username=User.objects.get(username=str(request.user))))
    inter = Interest.objects.filter(username=User.objects.get(username=str(request.user)))
    for i, obj in zip(range(1, 4), inter):
        k = 'interest_'+str(i)
        j = 'interest_'+str(i)+'_bio'
        l = 'interest_'+str(i)+'_link'
        prefill_dict[k] = obj.interest1
        prefill_dict[j] = obj.bio
        prefill_dict[l] = obj.link
        
    profile_form = ProfileForm(initial=prefill_dict)
    return render(request=request, template_name="main/profile.html", context={"profile_form":profile_form})