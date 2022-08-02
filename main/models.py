from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12) 
    postcode = models.CharField(max_length=12)
    message = models.TextField()


    def __str__(self):
        return f"{self.name} - {self.email}"


class Subscriber(models.Model):
    email = models.EmailField()

    def __str__(self):
        return f"{self.email}"

    class Meta:
        ordering = [ "-id" ]


class SubmittedProperties(models.Model):
    name = models.CharField(max_length=255)
    message = models.TextField()
    address = models.CharField(max_length=255)
    neighbour = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    budget = models.CharField(max_length=255)
    # image = models.FileField(blank=True, upload_to='properties/')

    email = models.EmailField()
    phone_number = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    message = models.TextField()

    property_type = models.CharField(max_length=255)
    land_status = models.CharField(max_length=255)

    # Features
    pool = models.BooleanField(default=False)
    gym = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.email}"

