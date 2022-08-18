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
            user = form.save()
            login()
            return redirect("main:profile")
        messages.error(request, "Invalid Informations!")
    form = NewUserForm()
    return render (request=request, template_name="main/signup.html", context={"register_form":form})