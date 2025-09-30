from django.contrib import admin
from . import models
# Register your models here.

class services_admin(admin.ModelAdmin):
    list_display=['__str__','is_active']
    list_editable=['is_active']

class plan_cart_admin(admin.ModelAdmin):
    list_display=['__str__','is_active']
    list_editable=['is_active']


class plan_title_admin(admin.ModelAdmin):
    list_display=['__str__','is_active']
    list_editable=['is_active']





admin.site.register(models.services,services_admin)
admin.site.register(models.plan_title,plan_title_admin)
admin.site.register(models.plan_cart,plan_cart_admin)