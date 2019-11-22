from django.db import models
from django.utils import timezone


class Kota(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class JobPosition(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    detail = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.name} -> {self.salary}'
    

class Employee(models.Model):

    nip = models.CharField(max_length=11,
            primary_key=True, null=False,
            blank=False, help_text="Nomor Induk Pegawai")

    name = models.CharField(max_length=40, blank=False,
            null=False, help_text="Nama Pegawai")

    # JABATAN = (
    #     ('Staff', 'Staff'),('Non Staff', 'Non Staff')
    # )

    job_position = models.ForeignKey(JobPosition, on_delete=models.SET_NULL, blank=True, null=True)

    GENDER = (('Male', 'Male'),('Female','Female'))

    gender = models.CharField(max_length=10, choices=GENDER,
        blank=False, null=True, help_text="Pilih Jenis Kelamin")

    date_of_birth = models.DateField(auto_now=False, null = True, default = '2019-11-06')
    place_of_birth = models.CharField(max_length=255, blank=False, null=True)
    address = models.TextField(max_length=50, blank=True,
        null=True, help_text="Masukkan Alamat Pegawai")    

    kota = models.ForeignKey(Kota, on_delete=models.CASCADE, blank=True, null=True)

    created = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True, null=True) 
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True, null=True)


    def __str__(self):
        return self.name


