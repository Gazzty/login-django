from django.shortcuts import render, redirect, HttpResponse
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy

# Create your views here.
def loginView(request, new_user=False):
    return render(request, 'core/login.html', {'new_user': new_user})

@csrf_protect
def loginResultView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = request.POST['password']
            print(username, password)
            # check that username exists
            if User.objects.filter(username=username).exists():
                print('User check')
                # Check that password is correct
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)    # Actual login
                    return render(request, 'core/login_result.html', {'login_ok': True, 'username': request.user})
                    
            
    print(form.errors)
    return render(request, 'core/login_result.html', {'login_ok': False})

@csrf_protect
def registerView(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            r_password = form.cleaned_data['r_password']

            if password != r_password:
                return HttpResponse('<h1>Password is not the same</h1>')

            new_user = User.objects.create_user(username=username, password=password, email=None)
            new_user.save()

            return render(request, 'core/login.html', {'new_user': True})

    return render(request, 'core/register.html')