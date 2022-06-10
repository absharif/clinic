from django.shortcuts import render
from .forms import Search
from .models import *
from django.db.models import Q
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
    return render(request, 'chamber/profile.html')


def profile_add(request):
    return render(request, 'chamber/profile_add.html')


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
