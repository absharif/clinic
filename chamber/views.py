from django.shortcuts import render

# Create your views here.


def search_profile(request):
    return render(request, 'chamber/search_profile.html')


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
