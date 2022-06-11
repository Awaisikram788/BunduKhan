from django.contrib import admin
from .models import *



class PropertyAdmin(admin.ModelAdmin):
    list = ('id', 'price', 'province', 'city')
    search_fields = ('id', 'price', 'province', 'area', 'city')
    autocomplete_fields = ['province', 'area', 'city']





admin.site.register(Property, PropertyAdmin)

admin.site.register(PropertyStatus)
admin.site.register(CarouselDisplay)
admin.site.register(Property_Type)