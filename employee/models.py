from django.db import models


class Employee(models.Model):
    
    nip = models.CharField(max_length=11, primary_key=True, null=False, blank=False)
    name = models.CharField(max_length=40, blank=False, null=True)

    JABATAN = (
        ('Staff', 'Staff'), ('Non Staff', 'Non Staff')
    )
    jabatan = models.CharField(max_length=15, choices=JABATAN, blank=False, null=False, default="Staff")

    def __str__(self):
        return self.name if self.name is not None else "Nama Default"
    