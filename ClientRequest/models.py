from django.db import models

# Create your models here.
class Quotation(models.Model):
    name = models.CharField(max_length= 100, null=False)
    meesage = models.TextField(null=False)
