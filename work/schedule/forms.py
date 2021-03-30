from django.contrib.admin.widgets import AdminDateWidget
from django.forms import ModelForm
from .models import Classwork
from django import forms

class ClassworkForm(ModelForm):
    class Meta:
        model = Classwork
        fields = ['day','date','subject','time']