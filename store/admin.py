from django.contrib import admin

# Register your models here.
from .models import motorcycle
from .models import motorcycleParts

class motorcycleAdmin(admin.ModelAdmin):
    list_display = [field.name for field in motorcycle._meta.fields]

class PartsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in motorcycleParts._meta.fields]



admin.site.register(motorcycle, motorcycleAdmin)
admin.site.register(motorcycleParts, PartsAdmin)