from django.shortcuts import render
from .forms import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate

# Create your views here.
def loginView(request):
    return render(request, 'core/login.html')

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
                user = authenticate(username=username, password=password)
                if user is not None:
                    return render(request, 'core/login_result.html', {'login_ok': True, 'username': username})
                    
            
    print(form.errors)
    return render(request, 'core/login_result.html', {'login_ok': False})