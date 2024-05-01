from django import forms

class BookingRequestForm(forms.Form):
    device_name = forms.CharField(max_length=100)
