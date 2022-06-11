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
            obj = int(obj.id)
        return HttpResponseRedirect(reverse('profile', args=[obj]))
    else:
        form = ProfileForm()
    return render(request, 'chamber/profile_add.html', {'form': form})


def profile_edit(request, id):
    obj = Profile.objects.get(id=id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.created_by = request.user
            obj.save()
            obj = int(obj.id)
        return HttpResponseRedirect(reverse('profile', args=[obj]))
    else:
        form = ProfileForm(instance=obj)
    return render(request, 'chamber/profile_add.html', {'form': form})


def profile_delete(request, id):
    return render(request, 'chamber/delete.html', {'id': id})


def profile_delete_confirm(request, id):
    obj = Profile.objects.get(id=id)
    obj.delete()
    return HttpResponseRedirect(reverse('search_profile'))


def prescription(request, id):
    pass


def prescription_add(request, profile_id):
    if request.method == 'POST':
        form = PrescriptionForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)

            obj.created_by = request.user
            profile_obj = Profile.objects.get(id=profile_id)
            obj.profile = profile_obj

            if 'pdf' in request.FILES:
                obj.pdf = request.FILES['pdf']
            if 'image' in request.FILES:
                obj.image = request.FILES['image']

            obj.save()
            obj = int(obj.profile.id)
        return HttpResponseRedirect(reverse('profile', args=[obj]))
    else:
        form = PrescriptionForm()
    return render(request, 'chamber/prescription_add.html', {'form': form})


def prescription_edit(request, profile_id, id):
    obj = Prescription.objects.get(id=id)
    if request.method == 'POST':
        form = PrescriptionForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
        return HttpResponseRedirect(reverse('profile', args=[profile_id]))
    else:
        form = PrescriptionForm(request.POST or None, instance=obj)
    return render(request, 'chamber/prescription_add.html', {'form': form})


def prescription_delete(request, profile_id, id):
    return render(request, 'chamber/prescription_delete.html', {'id': id, 'profile_id': profile_id})


def prescription_confirm_delete(request, profile_id, id):
    obj = Prescription.objects.get(id=id)
    obj.delete()
    return HttpResponseRedirect(reverse('profile', args=[profile_id]))