from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(label = 'Username', max_length=100, required=True)
    email = forms.EmailField(label = 'Email', max_length=100, required=True)
    password = forms.CharField(label = 'Password', max_length=100, required=True)
    confirmPassword = forms.CharField(label = 'Password', max_length=100, required=True)

class LoginForm(forms.Form):
    username = forms.CharField(label = 'Username', max_length=100, required=True)
    password = forms.CharField(label = 'Password', max_length=100, required=True)