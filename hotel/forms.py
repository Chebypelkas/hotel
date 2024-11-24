from django import forms
from .models import Passport


class Room(forms.Form):
    number = forms.IntegerField()
    name = forms.CharField(max_length=100)
    date = forms.DateField()


class PassportForm(forms.ModelForm):
    class Meta:
        model = Passport
        fields = ['number', 'number_ser', 'date_of_birth', 'name', 'last_name']
