from django.db import models

# Create your models here.
class RentalPropertyListing(models.Model):
   propertyName = models.CharField(max_length=100)
   location = models.CharField(max_length=100)
   rentAmount = models.IntegerField(default=0)
   ownerDetails = models.CharField(max_length=100)
   availabilityStatus = models.CharField(max_length=100)
   def __str__(self):
      return self.propertyName