from django.contrib import admin
from django.urls import path, include
from app.employee.views import Index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view()),
    path('employee/', include('app.employee.urls', namespace='employee-url')),
    path('payroll/', include('app.payroll.urls', namespace='payroll-url')),
]
