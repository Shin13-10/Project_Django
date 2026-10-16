
from django.db import models


class Member(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    membership_type = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    fee = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class Trainer(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
