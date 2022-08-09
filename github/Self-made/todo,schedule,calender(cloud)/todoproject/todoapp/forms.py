
from django import forms

class CalendarForm(forms.Form):
    start_date =forms.IntegerField(required=True)
    end_date = forms.IntegerField(required=True)
