# marketplace/admin.py
from django.contrib import admin
from .models import *

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'display_image')
    search_fields = ('name', 'description')
    list_filter = ('price',)

    def display_image(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" style="width: 50px; height: auto;">'
        return "No Image"
    display_image.allow_tags = True
    display_image.short_description = "Image"

admin.site.register(Category)
admin.site.register(BundledOffer)
# admin.site.register(FreelancerStory)
admin.site.register(ConsultationService)