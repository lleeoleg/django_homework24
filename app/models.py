from django.db import models

# Create your models here.

class Films(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    year = models.IntegerField()
    country = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title