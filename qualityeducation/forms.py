from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import qualityeducation, User

class qualityeducationForm(forms.ModelForm):
    class Meta:
        model = qualityeducation
        fields = ['title', 'description']

class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']