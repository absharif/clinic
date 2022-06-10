from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def home(request):
    return redirect('search_profile')


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


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('../login')
