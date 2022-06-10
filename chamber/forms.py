from django import forms


class Search(forms.Form):
    q = forms.CharField(max_length=120)


