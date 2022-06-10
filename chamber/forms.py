from django import forms
from .models import *


class Search(forms.Form):
    q = forms.CharField(max_length=120)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('created_by', 'created_at')


class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        exclude = ('profile', 'created_by', 'created_at')
