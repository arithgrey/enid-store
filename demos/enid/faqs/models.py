from django.db import models

# Create your models here.
class Faq(models.Model):
    ask = models.CharField(max_length=255)
    answer = models.TextField()
    is_visible = models.BooleanField(default=True)
    
    def __str__(self):
        return self.ask