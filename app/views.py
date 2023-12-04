from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from app.forms import RegistrationForm, LoginForm
from app.models import Form, Question, QuestionType

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/dashboard')
    return render(request, 'app/index.html')

def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/dashboard')

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
    
    if request.user.is_authenticated:
        return HttpResponseRedirect('/dashboard')
    return render(request, 'app/login.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login')

def dashboard_view(request):
    user_forms = Form.objects.filter(user=request.user).values()
    context = {'user_forms': user_forms}
    return render(request,'app/dashboard.html', context)

@login_required
def create_form(request):
    if request.method == "POST":
        user = request.user

        # Extract submitted form information
        title = request.POST.get('form_title')
        description = request.POST.get('form_description')

        # Create a new form for the user
        new_form = Form(user=user, title=title, description=description)
        new_form.save()

        # Add questions to this form
        question_texts = request.POST.getlist('question_text[]')
        question_types = request.POST.getlist('question_type[]')

        orderCount = 1
        for text, type_id in zip(question_texts, question_types):
            question_type = QuestionType.objects.get(id=type_id)
            question = Question(form=new_form, question_text=text, question_type=question_type, order=orderCount)
            question.save()
            orderCount += 1
        
        return HttpResponseRedirect('/dashboard')

    question_types = QuestionType.objects.all()
    context = {
        'question_types': question_types,

    }
    return render(request, 'app/createform.html', context)

@login_required
def get_form(request, form_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')
    
    # check if form is valid
    user_form = get_object_or_404(Form, pk=form_id)
    
    # check if form belongs to the user
    if user_form.user != request.user:
        return HttpResponseRedirect('/dashboard')
    
    # get all questions in the form
    questions = Question.objects.filter(form=user_form).order_by('order')
    # render the form with all of the questions in it
    context = {
        'title' : user_form.title,
        # 'form': user_form,
        'questions': questions
    }
    return render(request, 'app/form.html', context)