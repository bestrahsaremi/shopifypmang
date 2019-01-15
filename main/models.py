from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=120, blank=False)
    description = models.CharField(max_length=500, blank=True)
    vendor = models.CharField(max_length=120, blank=True),
    product_type = models.CharField(max_length=120, blank=False)
    tags = models.CharField(max_length=500, blank=False)

    def __str__(self):
        return self.name
