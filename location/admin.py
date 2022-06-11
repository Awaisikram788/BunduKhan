from django.contrib import admin
from .models import *
from import_export import resources


class ProvinceAdmin(admin.ModelAdmin):
    list = ('id', 'property')
    search_fields = ('id', 'property',)


class CityAdmin(admin.ModelAdmin):
    list = ('id', 'property__property', 'city')
    search_fields = ('id', 'property__property', 'city')


class AreaAdmin(admin.ModelAdmin):
    list = ('id', 'city__city', 'area')
    search_fields = ('id', 'city__city', 'area')


admin.site.register(Province, ProvinceAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Area, AreaAdmin)
