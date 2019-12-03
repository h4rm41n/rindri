from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.views import generic 
from django.urls import reverse_lazy
from django.forms.models import model_to_dict
from app.employee import forms, models


class FormMixin(object):
    form_class = forms.EmployeeForm
    model = models.Employee
    success_url = reverse_lazy('employee-url:list')


# class DeleteMixin:
    # def get_url(self):
        # object_meta = self.object._meta
        # names.append("%s/%s%s.html" % (
        #     object_meta.app_label,
        #     object_meta.model_name,
        #     self.template_name_suffix
        # ))
        # if self.url:
        #     return self.url
        # return None

    # def post(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     self.object.delete()

    #     return HttpResponseRedirect(reverse_lazy(self.get_url()))    


class Index(generic.TemplateView):
    template_name = "home.html"
 

class EmployeeCreateView(FormMixin, generic.CreateView):
    pass


class EmployeeListView(generic.ListView):
    queryset = models.Employee.objects.all().order_by('-name')


class EmployeeUpdate(FormMixin, generic.UpdateView):
    pass


class EmployeeDelete(generic.DeleteView):
    success_url = reverse_lazy("employee-url:list")
    model = models.Employee


class JobListView(generic.View):
    template_name = "employee/jobposition_list.html"

    def get(self, request):
        data = {
            "range": range(0,10),
            "job": models.JobPosition.objects.all()
        }
        return render(request, self.template_name, data)
        

class JobCreateView(generic.View):
    template_name = "employee/jobposition_form.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        form = request.POST
        obj = models.JobPosition()
        obj.name = form.get('name')
        obj.salary = form.get('salary')
        obj.detail = form.get('detail')
        obj.save()

        return redirect('employee-url:list-job')


class JobEditView(generic.View):
    template_name = "employee/jobposition_edit.html"

    def get(self, request, pk):
        obj = get_object_or_404(models.JobPosition, pk=pk)
        data = {
            "obj": obj
        }
        return render(request, self.template_name, data)

    def post(self, request, pk):
        form = request.POST
        obj = get_object_or_404(models.JobPosition, pk=pk)
        obj.name = form.get('name')
        obj.salary = form.get('salary')
        obj.detail = form.get('detail')
        obj.save(force_update=True)

        return redirect('employee-url:list-job')


class JobDeleteView(generic.DeleteView):
    model = models.JobPosition
    success_url = reverse_lazy("employee-url:list-job")