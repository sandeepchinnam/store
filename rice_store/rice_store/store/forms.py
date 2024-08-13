# store/forms.py
from django import forms

class CheckoutForm(forms.Form):
    name = forms.CharField(max_length=100, label='Full Name')
    address = forms.CharField(widget=forms.Textarea, label='Address')
    mobile_number = forms.CharField(max_length=15, label='Mobile Number')
from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['rice', 'quantity']  # Adjust fields as needed
