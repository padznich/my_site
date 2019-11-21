from django import forms

class CheckoutContactForm(forms.Form):
    cl_name = forms.CharField(required=True)
    cl_phone = forms.CharField(required=True)