from django import forms
from apps.tables.models import Table
from datetime import date


class DateForm(forms.Form):
    date = forms.DateField(initial=date.today().strftime("%Y-%m-%d"), widget=forms.DateInput(attrs={'id': 'datepicker'}))
    name = forms.CharField(max_length=155)
    email = forms.EmailField()