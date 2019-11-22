from django import forms
from app.payroll.models import Payroll


class PayRollForm(forms.ModelForm):
    class Meta:
        model = Payroll
        fields = '__all__'
