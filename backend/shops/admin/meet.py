from django.contrib import admin
from ..models import Meet


@admin.register(Meet)
class MeetAdmin(admin.ModelAdmin):
    search_fields = [
        'store__name',
        'store__employee__name',
    ]
