from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
# Create your views here.


def home(request):
    return redirect('login')


def user_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            return HttpResponseRedirect(reverse('search_profile'))
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            return render(request, 'website/login.html', {'invalid_login': "Invalid login details given"})
    return render(request, 'website/login.html')


def logout(request):
    return render(request, 'website/login.html')