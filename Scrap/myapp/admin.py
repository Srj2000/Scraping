from django.contrib import admin
from .models import NRI

@admin.register(NRI)
class NRIAdmin(admin.ModelAdmin):
    list_display=['id','details','publish']

# Register your models here.
