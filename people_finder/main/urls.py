from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("signup", views.signup_request, name="signup"),
    path("", views.login_request, name="login"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
    path("profile", views.profile_request, name="profile"),
    path("password_reset", views.password_reset_request, name="password_reset"),
    path("password_reset_profile", views.password_reset_profile_request, name="password_reset_profile"),
]
