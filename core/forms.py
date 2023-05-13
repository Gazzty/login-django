from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())

class RegisterForm(forms.Form):
    username = forms.CharField(label='username', max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())
    r_password = forms.CharField(widget=forms.PasswordInput())