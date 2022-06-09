from django.shortcuts import render, redirect

# Create your views here.


def home(request):
    return redirect('login')


def login(request):
    return render(request, 'website/login.html')


def logout(request):
    return render(request, 'website/login.html')