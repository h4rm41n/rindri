from django import forms
from employee.models import Employee


class DateInput(forms.DateInput):
    input_type = 'date'


class EmployeeForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=DateInput)

    class Meta:
        model = Employee
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'