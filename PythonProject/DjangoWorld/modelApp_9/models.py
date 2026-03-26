from django.db import models

# Create your models here.
class FeedbackAndReviewCollection(models.Model):
    rating = models.FloatField()
    comments = models.TextField()
    submissionDate = models.DateTimeField()
    reviewerName = models.TextField()
    def __str__(self):
        return self.reviewerName
