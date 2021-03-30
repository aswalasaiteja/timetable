from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import  authenticate,login as loginUser
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ClassworkForm

def home(request):
    form  = ClassworkForm()
    context = {
        'form' : form
    }
    return render(request, 'schedule/home.html', context=context)





def login(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        context = {
            'form': form
        }

        return render(request, 'schedule/login.html', context=context)
    else:
        form = AuthenticationForm(data = request.POST)
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            print("Authenticated: ", user)

            if user is not None:
                loginUser(request, user)
                return redirect('home')
        else:
            context = {
                'form': form
            }
            return render(request, 'schedule/login.html', context=context)


def register(request):
    if request.method == 'GET':
        form = UserCreationForm()
        context = {
            "form": form
        }
        return render(request, 'schedule/register.html', context=context)
    else:
        form = UserCreationForm(request.POST)
        context = {
            "form": form
        }
        if form.is_valid():
            user = form.save()
            print(user)
            if user is not None:
                return redirect('login')
        else:
            return render(request, 'schedule/register.html', context=context)


def add(request):
    form = ClassworkForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        return redirect('home')
    else:
        return render(request, 'home.html', context={'form':form})

def credentials(request):
    return render(request, 'schedule/credentials.html')


# Create your views here.
