from django.db import models
from app.employee.models import Employee


class Payroll(models.Model):

    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, blank=True, null=True)
    allowance = models.DecimalField(max_digits=10, decimal_places=2)
    overtime = models.DecimalField(max_digits=10, decimal_places=2)
    add_earnings = models.DecimalField(max_digits=10, decimal_places=2)
    thp = models.DecimalField(max_digits=10, decimal_places=2)
