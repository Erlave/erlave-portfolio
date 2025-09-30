from django.contrib import admin
from . import models
# Register your models here.

class hi_admin(admin.ModelAdmin):
    list_display = [ '__str__','is_active',]
    list_editable = [ 'is_active',]


class home_model_admin(admin.ModelAdmin):
    list_display = [ '__str__','is_active',]
    list_editable = [ 'is_active',]


admin.site.register(models.hi,hi_admin)
admin.site.register(models.home_model,home_model_admin)
