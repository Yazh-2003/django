from django.db import models

# Create your models here.
class CustomerSupportTicketSystem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    priority = models.CharField()
    Status = models.IntegerField()
    def __str__(self):
        return self.title