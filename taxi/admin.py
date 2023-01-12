from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Manufacturer, Driver, Car


admin.site.register(Manufacturer)


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = ["username", "email", "license_number"]
    fieldsets = UserAdmin.fieldsets + (('Additional info', {"fields": ("license_number",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional info', {"fields": ("license_number",)}),
    )


@admin.register(Car)
class AdminCar(admin.ModelAdmin):
    list_filter = ["manufacturer"]
    search_fields = ["model"]