from django import forms

from .models import EmployeeInfo



'''
define form from django form class
'''
 
class EmployeeInfoForm(forms.ModelForm):

	name   = forms.CharField(widget=forms.TextInput(attrs = {'class': 'form-control', 'required': 'true', 'autofocus':'true', 'placeholder':'First Name'}))
	email   = forms.CharField(widget=forms.EmailInput(attrs = {'class': 'form-control', 'required': 'true', 'autofocus':'true', 'placeholder':'Email'}))
	
	class Meta:
	    model = EmployeeInfo
	    fields = ('name', 'email')
