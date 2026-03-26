from django.db import models

# Create your models here.
class DailyExpenseTracker(models.Model):
    amount = models.IntegerField()
    category = models.CharField(max_length=100)
    paymentMode = models.CharField(max_length=100)
    date = models.DateField()
    def __str__(self):
        return self.category


