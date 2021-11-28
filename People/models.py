from django.db import models
from django.contrib.auth.models import User
gender_list = (('', 'Select'), ('M', 'Male'), ('F', 'Female'))

class Person(models.Model):
    id = models.AutoField('ID', primary_key=True)
    name = models.CharField("name", max_length=64)
    email = models.EmailField("Email", blank=True)
    headshot = models.ImageField(upload_to = 'img', blank = True)
    gender = models.CharField(max_length=1, choices=gender_list, default="")
    text = models.TextField('Desc', max_length=500, blank= True)
    friends = models.ManyToManyField('self', blank=True)
    
    def __str__(self):
        return f"{self.name}, {self.email}, Gender: {self.gender}, {self.friends}"