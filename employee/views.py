from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, TemplateView
from employee import forms, models


class Index(TemplateView):
    template_name = "home.html"


class EmployeeCreateView(CreateView):
    form_class = forms.EmployeeForm
    template_name = "form_employee.html"
    success_url = '/employee/'


class EmployeeList(ListView):
    queryset = models.Employee.objects.all().order_by('name')
    template_name = "list_employee.html"
