from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
# Create your views here.
# Hi this is views
#hiii


@login_required()
def homeView(request):
    template_name = 'app1/home.html'
    context = {}

    return render(request,template_name,context)



def signupView(request):
    template_name = 'app1/signup.html'
    form = UserCreationForm()

    if request.method=='POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()


    context = {'form':form}

    return render(request,template_name,context)

def loginView(request):
    template_name = 'app1/login.html'
    context = {}



    if request.method=='POST':
        un = request.POST.get('un')
        pw  = request.POST.get('pw')

        user = authenticate(username=un,password=pw)

        if user is not None:
            login(request,user)

            return redirect('homeview')


    return render(request,template_name,context)


def logutView(request):
    logout(request)

    return redirect('loginview')









