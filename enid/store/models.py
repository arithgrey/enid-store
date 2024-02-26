from django.db import models

class Store(models.Model):

    name = models.CharField(max_length=50)
    status = models.IntegerField(default=1)

    def __str__(self):
        return self.name