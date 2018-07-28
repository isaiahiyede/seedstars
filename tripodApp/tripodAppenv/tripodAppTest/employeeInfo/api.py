from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from employeeInfo.models import EmployeeInfo
from tastypie.authorization import DjangoAuthorization
from tastypie.authentication import BasicAuthentication
from tastypie import fields
from django.conf.urls import url
from django.shortcuts import render_to_response, render, redirect, get_object_or_404


"""
create an api endpoint to retreive all employee details
"""
class EmployeeInfoResource(ModelResource):
    class Meta:
        queryset = EmployeeInfo.objects.all()
        resource_name = 'employee/details'
        allowed_methods = ['get', 'post']
        # authorization = DjangoAuthorization()
        # authentication = BasicAuthentication()
        filtering = {
            'name': ['exact','in'],
        }

    # This method look for field "name" and apply upper on it
    def dehydrate_name(self, bundle):
        return bundle.data['name'].upper()