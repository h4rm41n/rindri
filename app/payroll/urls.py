from django.urls import path
from app.payroll import views

app_name = "payroll"

urlpatterns = [
    # path('', views.PayrollView.as_view(), name='list'),
    path('form/<str:nip>', views.PayrollView.as_view(), name="form"),
]
