from email.policy import default
from unicodedata import decimal
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=120) #max_length = required
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=10000)
    summary     = models.TextField(blank=True, null=False)
    featured    = models.BooleanField(default=True) # null=True, default=True
