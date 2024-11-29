from django.db import models
from state.models import State

class Address(models.Model):

    COUNTRY_CHOICES = (
    ('US', 'United States'),
    ('CA', 'Canada'),
    ('MX', 'Mexico'),        
    )

    street = models.TextField()
    colony = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100)    
    postal_code = models.CharField(max_length=10)
    country = models.CharField(
        max_length=2,
        choices=COUNTRY_CHOICES,
        default='MX'
    )

    delegation_or_municipality = models.TextField(blank=True, null=True)
    additional_details = models.TextField(blank=True, null=True)
    number = models.IntegerField()
    interior_number = models.IntegerField()

    state = models.ForeignKey(State, related_name="state_address", on_delete=models.CASCADE, null=False, blank=False)    
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state.name} {self.postal_code}, {self.country}"
