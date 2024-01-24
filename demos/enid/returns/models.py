from django.db import models

# Create your models here.
class Returns(models.Model):
    ask = models.CharField(max_length=255)
    short_answer = models.TextField(null=True, default=None)    
    path_seccion = models.CharField(max_length=255, null=True)
    call_to_action = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return self.ask