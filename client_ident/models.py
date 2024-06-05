from django.db import models

# Create your models here.

class ClientInfo(models.Model):
    client_id = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100,blank=True, null=True)
    longitude = models.CharField(max_length=100,blank=True, null=True)
    # latitude = models.DecimalField(max_digits=9, decimal_places=6,  blank=True, null=True)
    # longitude = models.DecimalField(max_digits=9, decimal_places=6,  blank=True, null=True)
    fingerprint = models.CharField(max_length=255,  blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client_id} - {self.latitude}, {self.longitude}"
