from django.db import models

# Create your models here.
class TaskAndDeadlinePlanner(models.Model):
    title = models.CharField(default=0, max_length=100)
    description = models.CharField(default=0, max_length=100)
    dueDate = models.DateField(default=0)
    priority = models.IntegerField(default=0)
    completionStatus = models.CharField(default=0)
    def __str__(self):
        return (self.title)

