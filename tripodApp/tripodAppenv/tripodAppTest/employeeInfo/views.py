from django.shortcuts import render_to_response, render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.template.context import RequestContext
from django import template
from .forms import EmployeeInfoForm
from .models import EmployeeInfo
from django.contrib import messages




# Create your views here.

"""
endpoint to display employee form
"""
def index(request):
	context = {}
	context['form'] = EmployeeInfoForm()
	template_name = "index.html"
	return render(request,template_name,context)


"""
endpoint to collect submitted data from interface and process it 
"""
def add_user(request):
	context = {}
	context['form'] = EmployeeInfoForm()
	template_name = "adduser.html"
	if request.method == "POST":
	    if request.POST.get('bot_catcher') != "":
	        return redirect(reverse('employee:index'))
	    else:
		    form = EmployeeInfoForm(request.POST)
		    if form.is_valid():
		    	messages.success(request,"Employee Details successfully added")
		    	return redirect(request.META['HTTP_REFERER'])
		    else:
	        	# print(form.errors)
	        	messages.error(request, "Please try again")        
	else:
		return render(request,template_name,context)


"""
endpoint to list all users
"""
def list_users(request):
	context = {}
	template_name = "userslist.html"
	all_user = EmployeeInfo.objects.all()
	context['all_users'] = all_user
	return render(request, template_name, context)















