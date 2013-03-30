from django import forms

class MensajeForm(forms.Form):
    message = forms.CharField(max_length=50)