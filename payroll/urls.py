from django.contrib import admin
from django.urls import path, include
from employee.views import Index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view()),
    path('employee/', include('employee.urls', namespace='employee-url')),
]
