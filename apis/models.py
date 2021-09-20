from django.db import models
from django import forms
from django.contrib.auth.models import User, Group

# Create your models here.
class UserMetas(models.Model):
    class Meta:
        db_table = 'all_users'
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    designation = models.CharField(max_length=100)
    def __str__(self):
        return self.name + ',' + self.email + ',' + self.designation