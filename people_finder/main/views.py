from contextlib import redirect_stderr
from django.shortcuts import render, redirect
from .form import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
# Create your views here.

def signup_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            print(form)
            user = form.save()
            # login(request, user)
            messages.success(request, "Signup successful." )
            return redirect("main:signup")
        messages.error(request, "Invalid Informations!")
    form = NewUserForm()
    return render (request=request, template_name="main/signup.html", context={"register_form":form})