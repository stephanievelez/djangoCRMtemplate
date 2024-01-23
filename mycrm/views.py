from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm


# Create your views here.
#login function
def home(request):
    if request.method == 'POST':
        username=request.POST['username']
        password = request.POST['password']
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully Logged In')
            return redirect('home')
        else:
            messages.success(request, 'Invalid Credentials')
            return redirect('home')
    else:
        return render(request, 'home.html')

    return render(request, 'home.html')

def logout_user(request):
    logout(request)
    messages.success(request, 'Successfully Logged Out')
    return redirect('home')


def Register_user(request):
    form = SignUpForm()
    if request.method =='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Registered')
            return redirect('home')
        else:
            messages.success(request, 'Invalid Credentials')
            return redirect('Register')
    else:
        form = SignUpForm()
        return render(request, 'Register.html', {'form':form})
    return render(request, 'Register.html')