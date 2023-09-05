from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(EventCreation)
class EventCreationAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_active']
    readonly_fields = ['link']

@admin.register(BookedSlot)
class BookedSlotAdmin(admin.ModelAdmin):
    list_display = ['id', 'event', 'start_time', 'end_time']