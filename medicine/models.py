from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Donor(models.Model):
    uname = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    phone = models.CharField(max_length = 200, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.uname.username

class NGO(models.Model):
    uname = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    phone = models.CharField(max_length = 200, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.uname.username

class Donations(models.Model):
    STATUS = (
        ('Pending','Pending'),
        ('Delivered','Delivered'),
    )
    donor = models.ForeignKey(Donor, on_delete = models.SET_NULL, null=True)
    ngo = models.ForeignKey(NGO, on_delete=models.SET_NULL, null=True)
    med_name = models.CharField(max_length=100, null=True)
    expiry_date = models.DateField(null=True)
    status = models.CharField(max_length = 200, null=True, choices=STATUS, default='Pending')


