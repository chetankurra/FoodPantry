from django import forms
from django.contrib.auth.models import User
from django.core import validators
from provider.models import *

class provider_form(forms.ModelForm):
    donor_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Provider Name '}))
    CHS = [('Individual', 'Individual'), ('Organisation', 'Organisation')]
    donor_status = forms.CharField(widget=forms.Select(attrs={'style':'display:inline;'},choices=CHS))
    CH = [('No', 'No'),('Yes', 'Yes')]
    anonymous_status = forms.CharField(widget=forms.Select(attrs={'style':'display:inline;'},choices=CH))
    class Meta():
	     model = provider
	     fields = '__all__'