from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'has_image',)
    list_filter = ('price',)
    search_fields = ('name', 'description')

    def has_image(self, obj):
        return bool(obj.image)
    has_image.boolean = True  # Show as a boolean icon in the admin
    has_image.short_description = 'Image Available'

admin.site.register(Service, ServiceAdmin)
