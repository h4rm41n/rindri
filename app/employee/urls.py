from django.urls import path, include
from app.employee import views

app_name = "employee"

urlpatterns = [
    path('', views.EmployeeListView.as_view(), name="list"),
    path('form/', views.EmployeeCreateView.as_view(), name="form"),
    path('edit/<str:nip>', views.EmployeeUpdate.as_view(), name="update"),
    path('delete/<str:nip>', views.EmployeeDelete.as_view(), name='delete'),


    path('job', views.EmployeeListView.as_view(), name="list-job"),
    path('form/', views.EmployeeCreateView.as_view(), name="form"),
    path('edit/<str:nip>', views.EmployeeUpdate.as_view(), name="update"),
    path('delete/<str:nip>', views.EmployeeDelete.as_view(), name='delete'),
]
