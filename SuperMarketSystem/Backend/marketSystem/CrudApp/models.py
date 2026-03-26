from django.db import models

# Create your models here.
class SuperMarketSystem(models.Model):
    productOne=models.CharField(max_length=200)
    productTwo=models.CharField(max_length=200)
    productThree=models.CharField(max_length=200)
    totalPrice=models.IntegerField()
    customerName=models.CharField(max_length=200)
    phoneNo=models.IntegerField()
    loyaltyPoints=models.IntegerField()
    def __str__(self):
        return self.customerName

