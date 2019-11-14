from django import forms
from .models import *
class Subscriber_form(forms.ModelForm):
    class Meta:
        model = Subscriber
        exclude = ['']