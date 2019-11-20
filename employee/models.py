from django.db import models


class Kota(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Employee(models.Model):

    nip = models.CharField(max_length=11,
            primary_key=True, null=False,
            blank=False, help_text="Nomor Induk Pegawai")

    name = models.CharField(max_length=40, blank=False,
            null=False, help_text="Nama Pegawai")

    JABATAN = (
        ('Staff', 'Staff'),('Non Staff', 'Non Staff')
    )

    job_Position = models.CharField(max_length=15,
            choices=JABATAN, blank=False, null=False,
            help_text="Jabatan Pegawai")

    GENDER = (('Male', 'Male'),('Female','Female'))

    gender = models.CharField(max_length=10, choices=GENDER,
        blank=False, null=True, help_text="Pilih Jenis Kelamin")

    date_of_birth = models.DateField(auto_now=False, null = True, default = '2019-11-06')
    place_of_birth = models.CharField(max_length=255, blank=False, null=True)
    address = models.TextField(max_length=50, blank=True,
        null=True, help_text="Masukkan Alamat Pegawai")    

    kota = models.ForeignKey(Kota, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


