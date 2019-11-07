from django.db import models

class Employee(models.Model):

    nip = models.CharField(max_length=11, primary_key=True, null=False, blank=False)
    name = models.CharField(max_length=40, blank=False, null=False)

    JABATAN = (
        ('Staff', 'Staff'),('Non Staff', 'Non Staff')
    )

    job_Position = models.CharField(max_length=15, choices=JABATAN, blank=False, null=False)

    GENDER = (('Male', 'Male'),('Female','Female'))

    gender = models.CharField(max_length=10, choices=GENDER, blank=False, null=True)

    date_of_birth = models.DateField(auto_now=False, null = True, default = '2019-11-06')

    address = models.CharField(max_length=50, blank=True, null=True)    

    def __str__(self):
        return self.name

