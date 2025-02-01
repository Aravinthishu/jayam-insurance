from django.contrib import admin
from .models import *



@admin.register(Social_links)
class SocialLinksAdmin(admin.ModelAdmin):
    search_fields = ('name', 'url')
    list_filter = ('name',)
    ordering = ('name',)
    fields = ('name', 'url', 'icon')


class AddressInline(admin.TabularInline):
    model = Address
    extra = 1  # Show one empty form initially
    fields = ['address']  # Only showing the address field for simplicity
    fk_name = 'brand'  # Ensures the address is linked to the correct Brand

# Brand admin with Address inline
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'address']  # Display fields for Brand
    inlines = [AddressInline]  # Add Address inline form to the Brand admin page

# Register the models with the admin site
admin.site.register(Brand, BrandAdmin)
admin.site.register(Address)

admin.site.register(updates)