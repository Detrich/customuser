from django.shortcuts import render, reverse, HttpResponseRedirect
from customuser.models import Myuser
from django.contrib.auth import logout, login, authenticate
from customuser.form import LoginUser , SignupUser
from django.contrib.auth.decorators import login_required
from project.settings import AUTH_USER_MODEL

# Create your views here.
@login_required
def index(request):
    data = Myuser.objects.first()
    return render(request, 'index.html', {'data':data, 'authuser': AUTH_USER_MODEL})

def login_request(request):
    if request.method == "POST":
        Form = LoginUser(request.POST)
        if Form.is_valid():
            data = Form.cleaned_data
            user = authenticate(username=data['username'],password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('homepage'))
    Form = LoginUser()
    return render(request, 'form.html', {'Form': Form})


def signup(request):
    if request.method == 'POST':
        Form = SignupUser(request.POST)
        if Form.is_valid():
            data = Form.cleaned_data
            user = Myuser.objects.create_user(
                username=data['username'],
                display_name=data['display_name'],
                password=data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('homepage'))
        return HttpResponseRedirect(reverse('homepage'))

    Form = SignupUser()
    return render(request,'form.html', {'Form': Form})


def logout_request(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))