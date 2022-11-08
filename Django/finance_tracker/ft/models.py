from django.db import models
from django.contrib.auth.models import User
import json
# Create your models here.

TYPE_CHOICES = (
    ('Credit','Credit'),
    ('Debit', 'Debit'),
)

class Expenses(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.CharField(max_length=8,blank=False,null=True)
    month = models.CharField(max_length=8,blank=False,null=True)
    year = models.CharField(max_length=8,blank=False,null=True)
    option = models.CharField(max_length=8,blank=False,null=True,choices=TYPE_CHOICES)
    amount = models.CharField(max_length=8,blank=False,null=True)
    def __str__(self):
        return str(self.user)
    

class Balance(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    current_balance = models.TextField(blank=True)
    total_balance = models.CharField(max_length=255,blank=True,default=0)
    def __str__(self):
        return str(self.user)
    