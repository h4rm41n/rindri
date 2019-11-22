from django.shortcuts import render, get_object_or_404
from django.views import generic
from .forms import PayRollForm
from app.employee.models import Employee


class PayrollView(generic.View):
    template_name = "payroll/form.html"

    def get(self, request, nip):
        employee = get_object_or_404(Employee, nip=nip)
        form = PayRollForm()
        data = {
            "form": form,
            "employee": employee
        }
        return render(request, self.template_name, data)
