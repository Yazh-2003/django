from django.db import models

# Create your models here.
class EventRegistrationManagement(models.Model):
    attendeeName = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 100)
    eventName = models.CharField(max_length = 100)
    registrationStatus = models.CharField(max_length = 100)
    def __str__(self):
        return self.attendeeName
