from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView, TemplateView, View
from django.forms.models import model_to_dict
from employee import forms, models


class Index(TemplateView):
    template_name = "home.html"


class EmployeeCreateView(CreateView):
    form_class = forms.EmployeeForm
    template_name = "employee/form_employee.html"
    success_url = '/employee/'


class EmployeeList(ListView):
    queryset = models.Employee.objects.all().order_by('name')
    template_name = "employee/list_employee.html"

class EmployeeEdit(View):
    def get(self, request, nip):
        template_name = "employee/edit.html"
        obj = get_object_or_404(models.Employee,nip=nip)
       
        form = forms.EmployeeForm(initial=model_to_dict(obj))
        data = { 
            "form" : form
        }

        return render(request, template_name, data)


