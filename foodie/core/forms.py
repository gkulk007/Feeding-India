from django import forms
from .models import Submitform


class Subm(forms.ModelForm):
    name = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=255)
    phone = forms.CharField(max_length=20)
    line = forms.CharField()

    class Meta:
        model = Submitform
        fields = ('name', 'email', 'phone', 'line')
