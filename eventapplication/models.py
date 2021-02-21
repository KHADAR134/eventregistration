from django.db import models
from django.contrib import admin
# Create your models here.

class Participants(models.Model):
    username=models.CharField(max_length=20)
    inst=models.CharField(max_length=20)
    email=models.CharField(max_length=40)
    contnum=models.CharField(max_length=15)

class ParticipantsAdmin(admin.ModelAdmin):
    list_display=("username","email","contnum") 