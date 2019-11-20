from django.urls import path, include
from employee import views

app_name = "employee"

urlpatterns = [
    path('', views.EmployeeList.as_view(), name="list"),
    path('form/', views.EmployeeCreateView.as_view(), name="form"),
]
