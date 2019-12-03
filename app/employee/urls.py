from django.urls import path, include
from app.employee import views

app_name = "employee"

urlpatterns = [
    path('employee', views.EmployeeListView.as_view(), name="list"),
    path('create', views.EmployeeCreateView.as_view(), name="create"),
    path('edit/<str:pk>', views.EmployeeUpdate.as_view(), name="update"),
    path('delete/<str:pk>', views.EmployeeDelete.as_view(), name='delete'),


    path('job', views.JobListView.as_view(), name="list-job"),
    path('job-create', views.JobCreateView.as_view(), name="create-job"),
    path('job-delete/<int:pk>', views.JobDeleteView.as_view(), name='delete-job'),
    path('job-edit/<int:pk>', views.JobEditView.as_view(), name="edit-job"),
    
]
