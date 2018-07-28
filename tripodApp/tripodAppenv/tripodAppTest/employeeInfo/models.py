from django.db import models
import datetime


# Create your models here.

'''
table to hold employee info
'''

class EmployeeInfo(models.Model):
	name = models.CharField(max_length=50, null=True, blank=True)
	email = models.CharField(max_length=50, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True)
	    
	def __str__(self):
	    return (f"{self.name}")
