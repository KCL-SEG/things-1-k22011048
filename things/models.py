from django.db import models

# Create your models here.
class Thing(models.MOdel):
    name = models.CharField(max_length=200)
    description = models.TextField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name
