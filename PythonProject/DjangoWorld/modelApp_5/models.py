from django.db import models

# Create your models here.
class RestaurantOrderManagement(models.Model):
    itemName = models.CharField(max_length = 100)
    itemQuantity = models.IntegerField()
    itemPrice = models.IntegerField()
    orderTime = models.DateTimeField()
    orderStatus = models.BooleanField()
    def __str__(self):
        return self.itemName