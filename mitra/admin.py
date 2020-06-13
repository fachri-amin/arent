from django.contrib import admin

# Register your models here.
from .models import AkunMitra,Iklan

class Read_only_fieds_Iklan(admin.ModelAdmin):
    readonly_fields = [
        'slug',
    ]

admin.site.register(AkunMitra)
admin.site.register(Iklan, Read_only_fieds_Iklan)