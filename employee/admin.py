from django.contrib import admin
from employee.models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'nip', 'job_Position']
    

admin.site.register(Employee, EmployeeAdmin)