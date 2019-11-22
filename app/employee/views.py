from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic 
from django.urls import reverse_lazy
from django.forms.models import model_to_dict
from app.employee import forms, models


class FormMixin(object):
    form_class = forms.EmployeeForm
    model = models.Employee
    success_url = reverse_lazy('employee:list')


class Index(generic.TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["label"] = "Aplikasi Kece"
        return context
 

class EmployeeCreateView(FormMixin, generic.CreateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["label"] = "Create"
        return context


class EmployeeListView(generic.ListView):
    queryset = models.Employee.objects.all().order_by('-name')


class EmployeeUpdate(FormMixin, generic.UpdateView):
    pk_url_kwarg = 'nip'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["label"] = "Update"
        return context


class EmployeeDelete(generic.View):
    def get(self, request, nip):
        obj = get_object_or_404(models.Employee, nip=nip)
        obj.delete()

        return redirect('employee:list')