from django.contrib import admin
from ..models import Store, Meet


class MeetInline(admin.TabularInline):
    model = Meet


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    inlines = [
        MeetInline,
    ]
    search_fields = [
        'name',
    ]
