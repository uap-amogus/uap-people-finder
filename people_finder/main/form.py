from socket import fromshare
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, ListofInterests, Interest
from django.forms import TextInput

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ("username", "email",)
    
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        
        if commit:
            user.save()
        return user

class ProfileForm(forms.Form):
           
    # class Meta:
    #     fields = ['first_name', 'last_name', 'display_picture',]
    #     widgets = {
    #         'first_name': TextInput(attrs={
    #             'class': 'form_input'}),
    #         'last_name': TextInput(attrs={
    #             'class': 'form_input'}),
    #         'display_picture': TextInput(attrs={
    #             'class': 'form_input'}),
    #         }
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)