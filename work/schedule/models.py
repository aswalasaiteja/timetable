from django.db import models
from django.contrib.auth.models import User
# Create your models here.
'''
Table Name: ClassWork
 Day ->choices
 Date
 Subject
 Time
 user
'''

class Classwork(models.Model):
    day_choices = [
        ('Sun','Sunday' ),
        ('Mon','Monday'),
        ('Tue','Tuesday'),
        ('Wed','Wednesday'),
        ('Thurs','Thursday'),
        ('Fri','Friday'),
        ('Sat','Saturday'),
    ]
    day = models.CharField(max_length=64, choices = day_choices)
    date = models.DateField()
    subject = models.CharField(max_length=64)
    time = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)





