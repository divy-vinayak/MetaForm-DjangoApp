from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from app.forms import RegistrationForm, LoginForm

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def register(request):
    if request.method == "POST":
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            data = registration_form.cleaned_data
            if data['password'] != data['confirmPassword']:
                return HttpResponse('invalid form submitted, password is not consistent')
            new_user = User.objects.create_user(username=data['username'], email=data['email'], password=data['password'])
            new_user.save()
            return HttpResponse("user created successfully! <a href='/login/'>Log In</a>")
        else:
            return HttpResponse("INVALID FORM SUBMITTED. TRY SIGNING UP AGAIN <a href='/register/'>SignUp</a>")
    return render(request, 'app/register.html')

def login_view(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            login_form_data = login_form.cleaned_data
            user = authenticate(username=login_form_data['username'], password=login_form_data['password'])
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/dashboard')
            else:
                return HttpResponse("INVALID CREDENTIALS. TRY LOGGING IN AGAIN <a href='/login/'>SignIn</a>")
        else:
            return HttpResponse("INVALID FORM SUBMITTED. TRY LOGGING IN AGAIN <a href='/login/'>SignIn</a>")

    return render(request, 'app/login.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login')

def dashboard_view(request):
    return render(request,'app/dashboard.html')