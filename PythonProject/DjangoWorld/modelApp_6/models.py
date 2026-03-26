from django.db import models

# Create your models here.
class PersonalHealthRecord(models.Model):
    visits = models.IntegerField(default=0)
    diagnosis = models.CharField(default=0, max_length=100)
    medicines = models.IntegerField(default=0)
    followDates = models.IntegerField(default=0)
    def __str__(self):
        return str(self.visits) + str(self.diagnosis)

