# authentication/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, LoginForm

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('log_in')
    else:
        form = SignUpForm()
    return render(request, 'authentication/sign_up.html', {'form': form})

def log_in(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'authentication/log_in.html', {'form': form})


from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'authentication/dashboard.html')

from django.contrib.auth import logout
def log_out(request):
    logout(request)
    return redirect('log_in')
