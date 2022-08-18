from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("signup", views.signup_request, name="signup")
]
