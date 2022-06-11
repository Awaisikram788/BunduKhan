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

