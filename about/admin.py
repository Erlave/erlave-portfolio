from django.contrib import admin
from . import models

# Register your models here.

class about_me_admin(admin.ModelAdmin):
    list_display = [ '__str__','is_active',]
    list_editable = [ 'is_active',]


class my_ability_admin(admin.ModelAdmin):
    list_display = [ '__str__','is_active',]
    list_editable = [ 'is_active',]


admin.site.register(models.about_me_model,about_me_admin)
admin.site.register(models.my_ability,my_ability_admin)