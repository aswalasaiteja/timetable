from django.contrib.admin.widgets import AdminDateWidget
from django.forms import ModelForm
from .models import Classwork
from django import forms
class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'


class ClassworkForm(ModelForm):
    class Meta:
        model = Classwork
        fields = ['day','date','subject','time']
        widgets = {
            'date' : DateInput(),
            'time' : TimeInput(),
        }
