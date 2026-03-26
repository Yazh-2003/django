from django.db import models

# Create your models here.
class AppointmentSlotManager(models.Model):
    date = models.DateField()
    time = models.TimeField()
    clientName = models.CharField(max_length=100)
    contactNumber = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    def __str__(self):
        return self.clientName
