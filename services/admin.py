from django.contrib import admin
from . import models
# Register your models here.

class services_admin(admin.ModelAdmin):
    list_display=['__str__','is_active']
    list_editable=['is_active']









admin.site.register(models.services,services_admin)