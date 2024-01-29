
from django.contrib import admin
from .models import Volunteer

@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone','message')
    search_fields = ('first_name', 'last_name', 'email', 'phone','message')