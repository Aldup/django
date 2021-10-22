from django import forms
from django.contrib.auth.models import User
from loginapp.models import UserProfileInfo



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ['first_name', 'last_name','username','email','password']

class UserprofileInfo(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        exclude = ['user',]
