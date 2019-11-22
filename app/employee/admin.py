from django.contrib import admin
from app.employee.models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'nip', 'job_position']
    

admin.site.register(Employee, EmployeeAdmin)