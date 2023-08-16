from django.db import models

# Create your models here.


class Emp(models.Model):
    EmpId = models.CharField(max_length=20)
    EmpName = models.CharField(max_length=20)
    EmpMail = models.EmailField(max_length=100)
    EmpPhoneNumber = models.IntegerField()

    def __str__(self) -> str:
        return self.EmpName