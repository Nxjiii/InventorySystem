from django.db import models
from django.utils import timezone


class User(models.Model):
    UserID = models.CharField(max_length=100)
    FirstName = models.CharField(max_length=100)
    Email = models.EmailField(max_length=250)
    Phone = models.IntegerField()
    Role = models.CharField(max_length=100)

class User_Admin(models.Model):
    AdminID = models.CharField(max_length=100)
    FirstName = models.CharField(max_length=100)
    Email = models.EmailField(max_length=250)
    Phone = models.IntegerField()
    Role = models.CharField(max_length=100)

class Hire_Reference(models.Model):
    RefID = models.IntegerField()
    Hire_StartDate = models.DateField(default=timezone.now)  # Set default to current date
    Hire_EndDate = models.DateField()  # End date will be calculated automatically
    Username = models.CharField(max_length=100)
    AdminUsername = models.CharField(max_length=100)
    HardwareID = models.CharField(max_length=100)
    Status = models.CharField(max_length=100, default='Status')

    def save(self, *args, **kwargs):
        # Automatically calculate Hire_EndDate as 20 days after Hire_StartDate
        self.Hire_EndDate = self.Hire_StartDate + timezone.timedelta(days=20)
        super().save(*args, **kwargs)

class Hardware(models.Model):
    HardwareID = models.IntegerField()
    DeviceName = models.CharField(null = False, max_length=200)
    DeviceType = models.CharField(null= False, max_length=100, default="DeviceType")
    Quantity = models.IntegerField()
    Audit = models.DateField(null = False, max_length=100)
    Location = models.CharField(null = False, max_length=200)
    Status = models.CharField(max_length=100)
    Warranty = models.CharField(max_length=100)
    Comments = models.TextField(null = True, max_length=1000)
    OnOffSite = models.CharField(null = True, max_length=100)
    RefID = models.IntegerField()

class NonElectronic_Hardware(models.Model):
    HardwareID = models.IntegerField()


class Electronic_Hardware(models.Model):
    DeviceName = models.CharField(null=True, max_length=200)
    DeviceType = models.CharField(null=True, max_length=100, default="DeviceType")
    HardwareID = models.IntegerField()
    DeviceSerial = models.CharField(max_length=100)
    CPU = models.CharField(max_length=100)
    GPU = models.CharField(max_length=100)
    RAM = models.CharField(max_length=100)
    Status = models.CharField(null=True, max_length=100, default= 'Status')
    Quantity = models.IntegerField( null=True, default= 0)