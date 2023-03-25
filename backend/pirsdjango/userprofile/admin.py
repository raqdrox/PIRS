from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'location')
    list_filter = ('user', 'name', 'location')
    search_fields = ('user', 'name', 'location')
    ordering = ('user', 'name', 'location')
    filter_horizontal = ()
    list_per_page = 25


admin.site.register(Profile, ProfileAdmin)


