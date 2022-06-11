from django.db import models
from location.models import *
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.
class PropertyStatus(models.Model):
    status = models.CharField(max_length=50)
    def __str__(self):
        return self.status
class CarouselDisplay(models.Model):
    status = models.CharField(max_length=50)
    def __str__(self):
        return self.status
class Property_Type(models.Model):
    Type= models.CharField(max_length=50)
    type_image = models.FileField(null=True, upload_to='properties/')
    def __str__(self):
        return self.Type
class Property(models.Model):
    name = models.CharField(max_length=50, default='Name Here')
    property_details = HTMLField()
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    price = models.BigIntegerField(default=None)
    header_display = models.ForeignKey(CarouselDisplay,on_delete=models.CASCADE,default=1)
    Property_Type = models.ForeignKey(Property_Type,on_delete=models.CASCADE,default=1)
    Year_Build = models.IntegerField(default=2000)
    propertyarea = models.IntegerField(default=0)
    bedrooms = models.IntegerField(default=0)
    livingrooms = models.IntegerField(default=0)
    status = models.ForeignKey(PropertyStatus, on_delete=models.CASCADE,default=1)
    washrooms = models.IntegerField(default=0)
    basement = models.IntegerField(default=False)
    garage = models.IntegerField(default=False)
    pool = models.IntegerField(default=False)
    floor_plan = models.FileField(blank=True, upload_to='properties/')
    full_house_image = models.FileField(blank=True, upload_to='properties/')
    image1 = models.FileField(blank=True, upload_to='properties/')
    image2 = models.FileField(blank=True, upload_to='properties/')
    image3 = models.FileField(blank=True, upload_to='properties/')
    image4 = models.FileField(blank=True, upload_to='properties/')
    image5 = models.FileField(blank=True, upload_to='properties/')
    creator = models.ForeignKey(User,on_delete=models.CASCADE,default=1)

    def __str__(self):
        return f"{self.province} - {self.price}"

    class Meta:
        ordering = ["-id"]


# class PropertyImage(models.Model):
#     ref_property = models.ForeignKey(Property, on_delete=models.CASCADE)
#     image = models.FileField(blank=True, upload_to='properties/')

#     def __str__(self):
#         return f"{self.ref_property_id}"

