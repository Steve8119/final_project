# authentication/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Student

class SignUpForm(UserCreationForm):
    class Meta:
        model = Student
        fields = ['username','full_name', 'admission_number', 'course', 'year_of_study', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    class Meta:
        model = Student
        fields = ['username', 'password']
