from django.contrib import admin
from ..models import Employee, Store


class StoreInline(admin.TabularInline):
    model = Store


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    inlines = [
        StoreInline,
    ]
    search_fields = [
        'pk',
        'phone_number',
    ]
