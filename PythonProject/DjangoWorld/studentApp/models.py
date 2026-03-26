from django.db import models


# Create your models here.
class studentModel(models.Model):
    studentName = models.CharField(max_length=100)
    admissionNo = models.IntegerField()
    standard= models.CharField()
    bloodGroup = models.CharField()
    address=models.CharField()
    def __str__(self):
        return self.studentName
