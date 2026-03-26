from django.db import models

# Create your models here.
class InventoryStockManagement(models.Model):
    stockQuantity = models.IntegerField()
    supplierName = models.CharField(max_length=100)
    purchaseDate = models.DateField()
    reorderLevel = models.IntegerField()
    def __str__(self):
        return self.supplierName