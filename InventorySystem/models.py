from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


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






def default_hire_end_date():
    return timezone.now() + timezone.timedelta(days=20)

class Hire_Reference(models.Model):
    Hire_StartDate = models.DateField(default=timezone.now)  
    Hire_EndDate = models.DateField(default=default_hire_end_date) 
    Username = models.CharField(max_length=100)
    DeviceName = models.CharField(max_length=100)
    HardwareID = models.CharField(max_length=100)
    Status = models.CharField(max_length=100, default='Booked')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk and not self.user_id: 
            self.user = User.objects.first()  

    def __str__(self):
        return f"{self.DeviceName} - {self.Hire_StartDate}"









  


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