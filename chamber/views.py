from django.shortcuts import render
from .forms import *
from .models import *
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
# Create your views here.


def search_profile(request):
    profile_list = []
    if request.method == 'POST':
        form = Search(data=request.POST)
        if form.is_valid():
            text = form.cleaned_data['q']

            try:
                obj = Profile.objects.get(id=text)
                if obj:
                    profile_list.append(obj)
            except:
                objects = Profile.objects.filter(Q(name__icontains=text) | Q(phone__icontains=text))
                if objects:
                    for obj in objects:
                        profile_list.append(obj)
    else:
        form = Search()
        objects = Profile.objects.all().order_by('-id')[:10]
        for obj in objects:
            profile_list.append(obj)

    return render(request, 'chamber/search_profile.html', {'form': form, 'profiles': profile_list})


def profile(request, id):
    profile_list = Profile.objects.get(id=id)
    prescriptions = Prescription.objects.filter(profile=profile_list).order_by('-created_at')
    return render(request, 'chamber/profile.html', {'profile': profile_list, 'prescriptions': prescriptions})


def profile_add(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.created_by = request.user
            obj.save()
            print(obj.id)
            obj = int(obj.id)
            print(type(obj))
            print(obj)
        return HttpResponseRedirect(reverse('profile', args=[obj]))
    else:
        form = ProfileForm()
    return render(request, 'chamber/profile_add.html', {'form': form})


def profile_edit(request, id):
    return render(request, 'chamber/profile_add.html')


def profile_delete(request, id):
    pass


def prescription(request, id):
    pass


def prescription_add(request):
    return render(request, 'chamber/prescription_add.html')


def prescription_edit(request, id):
    return render(request, 'chamber/profile_add.html')


def prescription_delete(request, id):
    pass
