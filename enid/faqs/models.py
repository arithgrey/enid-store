from django.db import models

# Create your models here.
class Faq(models.Model):
    ask = models.CharField(max_length=255)
    answer = models.TextField()
    is_visible = models.BooleanField(default=True)
    url_img = models.URLField(default=False)
    we_mean = models.TextField(null=True, default=None)    
    
    def __str__(self):
        return self.ask